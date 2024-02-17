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
    print('second stage!')
    user=anvil.users.get_user()
    if (user is None):
      user = app_tables.users.get(name='Admin')
    user_tokens=user['Push_Notification_Token']
    
    if user_tokens==None:
        user['Push_Notification_Token']=[token]
    else:
        user_tokens.append(token)
        user['Push_Notification_Token']=user_tokens

@anvil.server.callable
def send_notification():
    user=anvil.users.get_user()
    if (user is None):
      user = app_tables.users.get(name='Admin')
    user_tokens=user['Push_Notification_Token'] #Fetching all tokens of the current user
    
    from Push_Notifications import push_notifications
    
    title='An Example Title'
    body='This is some text'
    tag='tag'
    icon="https://cdn.pixabay.com/photo/2016/08/25/07/30/orange-1618917_960_720.png"
    badge="https://cdn.pixabay.com/photo/2016/08/25/07/30/orange-1618917_960_720.png"
    image="https://cdn.pixabay.com/photo/2018/01/12/14/24/night-3078326_960_720.jpg"
    click_url='https://anvil.works'
    buttons=[
    {'title':'Open Google','action':'https://google.com'},
    {'title':'Open YouTube','action':'https://youtube.com'},
    ]
    push_notifications.send(device_token=user_tokens,title=title,body=body)