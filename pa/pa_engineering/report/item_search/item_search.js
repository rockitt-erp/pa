// Copyright (c) 2016, Rockitt and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Search"] = {
	"filters": [
		{
			"label": __("Item Code"),
			"fieldtype": "Data",
			"fieldname": "item_code",
            "options": "",
            "default": ""
		},
		{
			"label": __("Item Name"),
			"fieldtype": "Data",
			"fieldname": "item_name",
            "default": ""
        },
		{
			"label": __("Item Group"),
			"fieldtype": "Link",
			"fieldname": "item_group",
			"options": "Item Group",
            "default": "All Item Groups"
		},
		{
			"label": __("Brand"),
			"fieldtype": "Link",
			"fieldname": "brand",
			"options": "Brand",
            "default": ""
		},
		{
			"label": __("Supplier"),
			"fieldtype": "Link",
			"fieldname": "supplier",
			"options": "Supplier",
            "default": ""
        }
	]
};
