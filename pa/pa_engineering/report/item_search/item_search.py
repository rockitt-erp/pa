# Copyright (c) 2013, Rockitt and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	filters = get_filters(frappe._dict(filters or {}))
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"label": _("Item Code"),
			"fieldtype": "Link",
			"fieldname": "item_code",
			"options": "Item",
			"width": 200
		},
		{
			"label": _("Item Name"),
			"fieldtype": "Data",
			"fieldname": "item_name",
			"width": 200
		},
		{
			"label": _("Item Group"),
			"fieldtype": "Link",
			"fieldname": "item_group",
			"options": "Item Group",
			"width": 200
		},
		{
			"label": _("Buying Price"),
			"fieldtype": "Currency",
			"fieldname": "buying_price",
			"options": "AUD",
			"width": 200
		},
		{
			"label": _("Selling Price"),
			"fieldtype": "Currency",
			"fieldname": "selling_price",
			"options": "AUD",
			"width": 200
		},
		{
			"label": _("Selling@1.6"),
			"fieldtype": "Currency",
			"fieldname": "selling_price_16",
			"options": "AUD",
			"width": 200
		},
		{
			"label": _("Selling@1.8"),
			"fieldtype": "Currency",
			"fieldname": "selling_price_18",
			"options": "AUD",
			"width": 200
		},
		{
			"label": _("Selling@2.0"),
			"fieldtype": "Currency",
			"fieldname": "selling_price_20",
			"options": "AUD",
			"width": 200
		},
				{
			"label": _("Brand"),
			"fieldtype": "Link",
			"fieldname": "brand",
			"options": "Brand",
			"width": 200
		},
		{
			"label": _("Supplier"),
			"fieldtype": "Link",
			"fieldname": "supplier",
			"options": "Supplier",
			"width": 200
		},
	]
	return columns

def surround_wildcard(str):
	return "%" + str + "%"

def get_filters(filters):
	conditions = []

	"""if filters.item_code:
		item_code = filters.item_code
		segments = item_code.split(" ")
		wildly = map(surround_wildcard, segments)
		wildcards = "".join(segmeents)
		conditions.append("i.item_code COLLATE UTF8_GENERAL_CI LIKE ")"""

	return conditions

def get_data(conditions):
	data = [{"item_code": "a"}]

	sql_query = 	"""
			SELECT * FROM `tabItem` i
			LEFT JOIN `tabItem Price` bip ON
				i.item_code = bip.item_code AND
				bip.price_list = 'Standard Buying'
			LEFT JOIN `tabItem Price` sip ON
				i.item_code = sip.item_code AND
				sip.price_list = 'Standard Selling'
			WHERE
			"""
	
	return data
