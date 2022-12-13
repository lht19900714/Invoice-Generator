import json

# Constants value and path
VAT_RATE_PATH = 'src/data/VAT.txt'
SHIPPING_RATE_PATH = 'src/data/shipping_rates.json'
VAT_RATE = 0

with open(VAT_RATE_PATH, 'r') as file:
	VAT_RATE = float(file.read().strip())


class Calculation:
	"""
	utility class to perform desired calculations in the cart
	"""

	@staticmethod
	def calculate_vat(items):
		"""
		:param items: list of items in the cart
		:return: VAT amount, rounded to 2 decimal places

		calculate the VAT of the cart based on the VAT rate
		"""
		vat_res = 0
		for item in items:
			vat_res += item.get_item_original_price() * VAT_RATE
		return round(vat_res, 2)

	@staticmethod
	def calculate_shipping_cost(items):
		"""
		:param items: list of items in the cart
		:return: shipping cost, rounded to 2 decimal places

		calculate the shipping cost of the cart based on the shipping rates and the items' weight
		"""
		shipping_rates = {}
		shipping_cost = 0

		with open(SHIPPING_RATE_PATH, 'r') as shipping_rate_file:
			shipping_rates = json.load(shipping_rate_file)

		for item in items:
			shipping_cost += item.get_item_weight() * shipping_rates[item.get_item_country()]
		return round(shipping_cost, 2)
