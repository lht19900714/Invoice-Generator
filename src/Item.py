
class Item:
	"""
	Item class is used to store the information of each product item.
	It is immutable, so we don't need to implement setter methods.
	"""
	def __init__(self, item_type, item_price, item_shipped_from, item_weight):
		self._item_type = item_type
		self._item_price = item_price
		self._item_shipped_from = item_shipped_from
		self._item_weight = item_weight

	def get_item_type(self):
		return self._item_type

	def get_item_price(self):
		return self._item_price

	def get_item_shipped_from(self):
		return self._item_shipped_from

	def get_item_weight(self):
		return self._item_weight
