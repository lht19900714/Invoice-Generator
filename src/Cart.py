import json
from src.Discount import discount_status, shipping_discount
from collections import defaultdict

# Constants value and path
VAT_RATE = 0.14
SHIPPING_RATE_PATH = 'src/data/shipping_rates.json'
PRODUCTS_PATH = 'src/data/products.json'

products = json.load(open(PRODUCTS_PATH, 'r'))


class Cart:
	"""
	Cart class is responsible for calculating the total price of the cart.
	It has a list of items and can calculate the total price and apply discounts.
	"""

	def __init__(self, items: list):
		self._items = items
		self._items_counts = 0
		self._items_details = defaultdict(lambda: [0, 0, '', 0])  # [price, count, country, weight]
		self._sub_total = 0
		self._shipping_cost = 0
		self._VAT = 0
		self._discount_amount = 0
		self._discount_details = defaultdict(lambda: [0, ''])  # [amount, title]
		self._total = 0

		self.process_items()
		self.post_process()

	def calculate_discount(self):
		"""
		Apply discounts to the cart.
		:return: None
		"""
		for discount_name in discount_status:
			if discount_status[discount_name]:
				amount, title = discount_name(self._items_details)
				self._discount_details[discount_name] = [amount, title]

		self._discount_details['shipping_discount'] = shipping_discount(self._items_counts, self._shipping_cost)
		self._discount_amount = sum(details[0] for details in self._discount_details.values())

	def calculate_total(self):
		"""
		Calculate the total price of the cart.
		:return: None
		"""
		self._total = self._sub_total + self._shipping_cost + self._VAT - self._discount_amount

	def get_items_counts(self):
		"""
		Calculate the number of items in the cart.
		:return: None
		"""
		self._items_counts = sum(item_datails[1] for item_datails in self._items_details.values())

	def get_items_details(self):
		"""
		Get the details of the items and put them in a dictionary.
		The format of dictionary is {item_type: [price, count, country, weight]}
		:return: None
		"""
		for item in self._items:
			self._items_details[item.get_item_type()][0] = item.get_item_price()
			self._items_details[item.get_item_type()][1] += 1
			self._items_details[item.get_item_type()][2] = item.get_item_shipped_from()
			self._items_details[item.get_item_type()][3] = item.get_item_weight()

	def calculate_sub_total(self):
		"""
		Calculate the sub total of the cart.
		:return: None
		"""
		self._sub_total = sum(item_datails[0] * item_datails[1] for item_datails in self._items_details.values())

	def calculate_shipping_cost(self):
		"""
		Calculate the shipping cost of the cart.
		:return: None
		"""
		shipping_rate = json.load(open(SHIPPING_RATE_PATH))
		self._shipping_cost = sum(
			shipping_rate[item_details[2]] * item_details[3] * 10 for item_details in self._items_details.values())

	def calculate_VAT(self):
		"""
		Calculate the VAT of the cart.
		:return: None
		"""
		self._VAT = sum(item_datails[0] * item_datails[1] * VAT_RATE for item_datails in self._items_details.values())

	def process_items(self):
		"""
		Process the items in the cart and calculate subtotal, shipping cost, VAT, and apply available discount.
		:return: None
		"""
		self.get_items_details()
		self.get_items_counts()
		self.calculate_sub_total()
		self.calculate_shipping_cost()
		self.calculate_VAT()
		self.calculate_discount()
		self.calculate_total()

	def post_process(self):
		"""
		Post process the cart after calculating the total price.
		Since all amounts are currency amount, so round them to 2 decimal places.
		:return: None
		"""
		for item_detail in self._items_details:
			self._items_details[item_detail][0] = round(self._items_details[item_detail][0], 2)

		for discount_details in self._discount_details:
			self._discount_details[discount_details][0] = round(self._discount_details[discount_details][0], 2)

		self._sub_total = round(self._sub_total, 2)
		self._shipping_cost = round(self._shipping_cost, 2)
		self._VAT = round(self._VAT, 2)
		self._discount_amount = round(self._discount_amount, 2)
		self._total = round(self._total, 2)

	def get_cart_invoice(self):
		"""
		Get the invoice of the cart.
		:return:
		"""
		discount = ''
		for discount_name in self._discount_details:
			if self._discount_details[discount_name][0] != 0:
				discount += f'\t{self._discount_details[discount_name][1]}: -${self._discount_details[discount_name][0]}\n'
		discount = discount.rstrip('\n')
		invoice = f'''
Subtotal: {self._sub_total}
Shipping: {self._shipping_cost}
VAT: {self._VAT}'''
		if discount != '':
			invoice += f'''\nDiscounts:
{discount}'''
		invoice += f'''\nTotal: {self._total}'''
		return invoice
