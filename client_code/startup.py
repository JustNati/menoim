import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Main import Main
from anvil_extras import routing
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
try:
  from Push_Notifications import firebase
except:
  print('You have not added Push Notifications dependency yet. Generate one by visiting https://push-notifications.anvil.app')

try:
  token=firebase.request_push_notifications()
  if firebase.not_exists(token): #Ensuring that the device is not already registered
    anvil.server.call('store_token',token) #Now we can store the token
except:
  print('Push Notifications are not supported on your browser. Please use a different browser')
  
routing.set_url_hash("", replace_current_url=True)
routing.launch()
