# Copyright (c) 2026, sorn-weeraphat and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseRecord(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		category: DF.Literal["\u0e04\u0e48\u0e32\u0e2d\u0e32\u0e2b\u0e32\u0e23", "\u0e04\u0e48\u0e32\u0e40\u0e14\u0e34\u0e19\u0e17\u0e32\u0e07", "\u0e04\u0e48\u0e32\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c"]
		expense_date: DF.Date
		item_name: DF.Data
		receipt: DF.Attach | None
	# end: auto-generated types

	pass
