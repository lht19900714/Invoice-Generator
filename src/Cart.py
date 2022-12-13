from src.Calculation import Calculation
from src.Discount import Discount


class Cart:
	"""
	Cart class is responsible for calculating the total price of the cart.
	It has a list of items and can calculate the total price and apply discounts.
	"""

	def __init__(self, items):
		self._items = items
		self._items_counts = len(items)
		self._shipping_cost = 0
		self._discount_details = {}  # {title, amount}
		self._sub_total = 0
		self._total = 0

		self.process_items()
		self.calculate_discount()
		self.calculate_total()

	def add_item(self, item):
		"""
		:param item: Item object
		:return: None

		Add an item to the cart.
		"""
		self._items.append(item)
		self._items_counts += 1

	def remove_item(self, item):
		"""
		:param item: Item object
		:return: None

		Remove an item from the end of cart list. If the item is not in the list, do nothing.
		"""
		for i in range(self._items_counts, -1, -1):
			if self._items[i] == item:
				self._items.pop(i)
				self._items_counts -= 1
				break

	def get_items_counts(self):
		"""
		:return: int

		Get the number of items in the cart.
		"""
		return self._items_counts

	def get_shipping_cost(self):
		"""
		:return: float

		Get the shipping cost of the cart.
		"""
		return self._shipping_cost

	def get_all_items(self):
		"""
		:return: list of Item objects

		Get all items in the cart.
		"""
		return self._items

	def process_items(self):
		"""
		:return: None

		Calculate subtotal, shipping cost and VAT, then save them in the cart object.
		"""
		self._sub_total = sum(item.get_item_original_price() for item in self._items)
		self._shipping_cost = Calculation.calculate_shipping_cost(self._items)
		self._VAT = Calculation.calculate_vat(self._items)

	def calculate_discount(self):
		"""
		:return: None

		Apply discounts to the cart.
		"""

		static_methods = [method for method in dir(Discount) if
		                  callable(getattr(Discount, method)) and not method.startswith('_')]

		for method in static_methods:
			amount, title = getattr(Discount, method)(self)
			self._discount_details[title] = amount

	def calculate_total(self):
		"""
		:return: None

		Calculate the total price of the cart.
		"""
		discount_amount = sum(self._discount_details.values())
		self._total = self._sub_total + self._shipping_cost + self._VAT - discount_amount

	def get_cart_invoice(self):
		"""
		:return: None

		Get the invoice for the cart.
		"""
		discount = ''
		for title, amount in self._discount_details.items():
			if amount > 0:
				discount += f'\t{title}: -${amount}\n'
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
