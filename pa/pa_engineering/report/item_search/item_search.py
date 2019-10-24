# Copyright (c) 2013, Rockitt and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	conditions = get_conditions(frappe._dict(filters or {}))
	columns = get_columns()
	data = get_data(conditions)
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
			"label": _("Brand"),
			"fieldtype": "Link",
			"fieldname": "brand",
			"options": "Brand",
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
			"label": _("RRP"),
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
			"label": _("Item Group"),
			"fieldtype": "Link",
			"fieldname": "item_group",
			"options": "Item Group",
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

def get_conditions(filters):
	conditions = []
	arguments = []

	if filters.item_code:
		item_code = filters.item_code
		segments = map(surround_wildcard, item_code.split(" "))

		item_code_clauses = []
		for segment in segments:
			clause = "LOWER(i.item_code) LIKE LOWER(%s)"
			item_code_clauses.append(clause)
			arguments.append(segment)

		item_code_condition = " OR ".join(item_code_clauses)
		item_code_condition = "(" + item_code_condition + ")"
		conditions.append(item_code_condition)

	if filters.item_name:
		item_name = filters.item_name
		segments = map(surround_wildcard, item_name.split(" "))

		item_name_clauses = []
		for segment in segments:
			clause = "LOWER(i.item_name) LIKE LOWER(%s)"
			item_name_clauses.append(clause)
			arguments.append(segment)
		
		item_name_conditon = " AND ".join(item_name_clauses)
		item_name_conditon = "(" + item_name_conditon + ")"
		conditions.append(item_name_conditon)
	
	if filters.item_group:
		conditions.append("i.item_group = %s")
		arguments.append(filters.item_group)

	if filters.brand:
		conditions.append("i.brand = %s")
		arguments.append(filters.brand)

	if filters.supplier:
		conditions.append("i.default_supplier = %s")
		arguments.append(filters.supplier)

	condition = " AND ".join(conditions)
	return (condition, arguments)

def get_data(conditions):
	sql_query = 	"""
			SELECT 
				i.item_code as "item_code", 
				i.item_name as "item_name", 
				i.item_group as "item_group", 
				bip.price_list_rate as "buying_price",
				sip.price_list_rate as "selling_price",
				bip.price_list_rate * 1.6 as "selling_price_16",
				bip.price_list_rate * 1.8 as "selling_price_18",
				bip.price_list_rate * 2.0 as "selling_price_20",
				i.brand as "brand",
				i.default_supplier as "supplier"
			FROM `tabItem` i
				LEFT JOIN `tabItem Price` bip ON
					bip.item_code = i.item_code AND 
					bip.price_list = 'Standard Buying'
				LEFT JOIN `tabItem Price` sip ON
					sip.item_code = i.item_code AND 
					sip.price_list = 'Standard Selling'
			"""
	
	condition, arguments = conditions

	if bool(condition):
		sql_query += "WHERE " + condition

	sql_query += "\nLIMIT 1000"

	data = frappe.db.sql(sql_query, arguments, as_dict=True)
	return data