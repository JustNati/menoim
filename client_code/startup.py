import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Main import Main
from anvil_extras import routing
from Push_Notifications import firebase
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
routing.set_url_hash("", replace_current_url=True)
routing.launch()
