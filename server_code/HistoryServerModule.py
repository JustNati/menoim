import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_powertest():
  return app_tables.powertests.search()
  
@anvil.server.callable
def store_token(token):
    user=anvil.users.get_user()
    user_tokens=user['Push_Notification_Token']
    
    if user_tokens==None:
        user['Push_Notification_Token']=[token]
    else:
        user_tokens.append(token)
        user['Push_Notification_Token']=user_tokens