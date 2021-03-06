# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "combine_app"
app_title = "Combine App"
app_publisher = "korecent"
app_description = "combine"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "rohit@korecent.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/combine_app/css/combine_app.css"
# app_include_js = "/assets/combine_app/js/combine_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/combine_app/css/combine_app.css"
# web_include_js = "/assets/combine_app/js/combine_app.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "combine_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "combine_app.install.before_install"
after_install = "combine_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "combine_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
	"Sales Invoice": {
		"validate": "frappe.email.doctype.email_group.email_group.restrict_email_group"
	 },
 }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"combine_app.tasks.all"
# 	],
# 	"daily": [
# 		"combine_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"combine_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"combine_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"combine_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "combine_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "combine_app.event.get_events"
# }

