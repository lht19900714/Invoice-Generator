import json

# Constants path
SHIPPING_DISCOUNT_SETTING_PATH = 'src/data/shipping_discount_setting.json'
SHOE_DISCOUNT_SETTING_PATH = 'src/data/shoe_discount_setting.json'
TOPS_DISCOUNT_SETTING_PATH = 'src/data/tops_discount_setting.json'


class Discount:
	"""
	Discount class include discount calculation for items in the cart
	"""

	@staticmethod
	def calculate_shoes_discount(cart):
		"""
		:param cart: cart object
		:return: discount amount and discount title

		calculate shoes discount price for the cart based on the discount setting.
		Each item in the cart will be checked if it is shoes, if it is shoes, the discount will be applied.
		"""
		total_discount_amount = 0
		shoe_discount_setting = json.load(open(SHOE_DISCOUNT_SETTING_PATH, 'r'))
		shoe_discount_percentage = shoe_discount_setting['discount_percentage']
		for item in cart.get_all_items():
			if item.get_item_name() == 'Shoes':
				discount_amount = item.get_item_original_price() * shoe_discount_percentage
				discounted_price = item.get_item_original_price() * (1 - shoe_discount_percentage)
				item.set_item_discount_price(discounted_price)
				total_discount_amount += discount_amount
		return [round(total_discount_amount, 2), f'{int(shoe_discount_percentage * 100)}% off shoes']

	@staticmethod
	def shipping_discount(cart):
		"""
		:param cart: cart object
		:return: list of discount amount and discount description

		calculate shipping cost discount for the cart based on the discount setting.
		If there are more than required count items in the cart, the shipping cost will be discounted by the discount amount.
		"""
		discounted_amount = 0
		shipping_discount_setting = json.load(open(SHIPPING_DISCOUNT_SETTING_PATH, 'r'))
		discount_amount = shipping_discount_setting['discount_amount']
		required_count = shipping_discount_setting['required_count']
		shipping_cost = cart.get_shipping_cost()
		items_counts = cart.get_items_counts()
		if items_counts >= required_count:
			discounted_amount = min(shipping_cost, discount_amount)
		return [round(discounted_amount, 2), f'${discounted_amount} off shipping']

	@staticmethod
	def tops_discount(cart):
		"""
		:param all_items: a list of all items in the cart
		:return: list of discount amount(rounded to 2 decimal places) and discount description

		calculate tops discount for the cart based on the discount setting.
		If there are more than 2 tops in the cart, the target item will be discounted by 50%.
		"""
		total_discount_amount = 0
		tops_count = 0
		target_item_count = 0
		target_item_original_price = 0
		tops_discount_setting = json.load(open(TOPS_DISCOUNT_SETTING_PATH, 'r'))
		discount_percentage = tops_discount_setting['discount_percentage']
		target_item_name = tops_discount_setting['target_item_name']
		required_count = tops_discount_setting['required_count']
		all_items = cart.get_all_items()
		for item in all_items:
			if item.get_item_category() == 'tops' and item.get_item_name() != target_item_name:
				tops_count += 1
			elif item.get_item_name() == target_item_name:
				target_item_count += 1
				target_item_original_price = item.get_item_original_price()

		cursor = cart.get_items_counts() - 1
		while tops_count >= required_count and target_item_count > 0 and cursor > 0:
			if all_items[cursor].get_item_name() == target_item_name:
				discount_amount = target_item_original_price * discount_percentage
				discounted_price = target_item_original_price * (1 - discount_percentage)
				all_items[cursor].set_item_discount_price(discounted_price)
				total_discount_amount += discount_amount
				target_item_count -= 1
				tops_count -= required_count
			cursor -= 1

		return [round(total_discount_amount, 2), f'{int(discount_percentage * 100)}% off {target_item_name}']
