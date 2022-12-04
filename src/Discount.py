'''
@File   :  Discount.py
@Author :  Haitao Lu
@Date   :  03-Dec-2022 12:05 PM
'''


def shoes_discount(all_items: dict):
	"""
	:param all_items: a dictionary of all items in the cart
	:return: list of discount amount and discount description
	"""
	if 'Shoes' in all_items:
		return [all_items['Shoes'][0] * all_items['Shoes'][1] * 0.1, '10% off shoes']
	else:
		return [0, '10% off shoes']


def shipping_discount(items_count: int, shipping_cost: float):
	"""
	:param items_count: number of items in the cart
	:param shipping_cost: shipping cost of the cart
	:return: list of discount amount and discount description
	"""
	if items_count >= 2 and shipping_cost >= 10:
		return [10, '$10 off shipping']
	else:
		return [0, '$10 off shipping']


def tops_discount(all_items: dict):
	"""
	:param all_items: a dictionary of all items in the cart
	:return: list of discount amount and discount description
	"""
	res = 0
	tops_count = 0
	jacket_count = 0
	jacket_price = 0
	for item_type, item_detail in all_items.items():
		if item_type == 'T-shirt' or item_type == 'Blouse':
			tops_count += 1
		elif item_type == 'Jacket' and jacket_count == 0:
			jacket_count += 1
			jacket_price = item_detail[0]
	if tops_count >= 2:
		res = jacket_price * 0.5
	return [res, '50% off jacket']


discount_status = {
	shoes_discount: True,
	tops_discount: True
}
