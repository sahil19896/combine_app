from __future__ import unicode_literals
from os import system, getcwd, environ, path
import frappe

USER = "/home/" + environ['USER']
FBENCH = path.join(USER, "frappe-bench")
APPS = path.join(USER, "frappe-bench/apps")

def after_install():
	frappe.db.set_default('desktop:home_page', '')
	frappe.db.commit()

	print "**************after install*******************"

	system("cp " + path.join(APPS, "combine_app/sales_invoice_list.js") + " " +  path.join(APPS, "erpnext/erpnext/account/doctype/sales_invoice"))
