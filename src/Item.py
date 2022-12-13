class Item:
	"""
	Item class represents a product item.

	Item class has 6 attributes:
	_item_name: the type of the item, e.g. T-shirt, Blouse, Pants, Shoes, Jacket
	_item_original_price: the original price of the item
	_item_discount_price: the discounted price of the item
	_item_country: the country where the item is shipped from
	_item_weight: the weight of the item
	_item_category: the category of the item, e.g. tops, bottoms
	"""

	def __init__(self, item_name, item_price, item_country, item_weight, item_category):
		self._item_name = item_name
		self._item_original_price = item_price
		self._item_discount_price = item_price
		self._item_country = item_country
		self._item_weight = item_weight
		self._item_category = item_category

	def get_item_name(self):
		return self._item_name

	def get_item_original_price(self):
		return self._item_original_price

	def get_item_country(self):
		return self._item_country

	def get_item_weight(self):
		return self._item_weight

	def get_item_category(self):
		return self._item_category

	def get_item_discount_price(self):
		return self._item_discount_price

	def set_item_discount_price(self, new_price):
		self._item_discount_price = new_price
