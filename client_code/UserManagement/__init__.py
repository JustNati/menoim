from ._anvil_designer import UserManagementTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('UserManagement')
class UserManagement(UserManagementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.submiter_dd.items = sorted([r['name'] for r in app_tables.users.search(is_submiter=True)])
    self.approver_dd.items = sorted([r['name'] for r in app_tables.users.search(is_approver=True)])
    # Any code you write here will run before the form opens.

  def clear_data():
    self.reg_user.text= ''
    self.approver.text=''
    self.submiter_dd.items = sorted([r['name'] for r in app_tables.users.search(is_submiter=True)])
    self.approver_dd.items = sorted([r['name'] for r in app_tables.users.search(is_approver=True)])
  
  def add_reg_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (app_tables.users.get(name=self.reg_user.text, is_submiter=True)):
      Notification("קיים כבר במערכת",
             title="לא ניתן לבצע פעולה זו",
             style="danger").show()
    else:
       new_row = app_tables.users.add_row(name=self.reg_user.text, is_submiter=True, is_moderator=False, is_approver=False)
       Notification("הוסף מבצע",
              title="!פעולה בוצעה",
              style="success").show()
       self.clear_data()

  def add_approver_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (app_tables.users.get(name=self.approver.text, is_approver=True)):
      Notification("קיים כבר במערכת",
             title="לא ניתן לבצע פעולה זו",
             style="danger").show()
    elif (app_tables.users.get(name=self.approver.text, is_approver=False)):
      user = app_tables.users.get(name=self.approver.text)
      user['is_approver'] = True
      Notification("עודכן בודק",
              title="!פעולה בוצעה",
              style="success").show()
      self.clear_data()
    else:
      new_row = app_tables.users.add_row(name=self.approver.text, is_submiter=True, is_moderator=False, is_approver=True)
      Notification("הוסף בודק",
              title="!פעולה בוצעה",
              style="success").show()
      self.clear_data()

  def remove_reg_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_to_remove = app_tables.users.get(name=self.submiter_dd.selected_value)
    user_to_remove.delete()
    Notification("נמחק בודק",
              title="!פעולה בוצעה",
              style="success").show()
    self.clear_data()

  def remove_approver_click(self, **event_args):
    """This method is called when the button is clicked"""
    user_to_remove = app_tables.users.get(name=self.approver_dd.selected_value)
    user_to_remove.delete()
    Notification("נמחק מבצע",
              title="!פעולה בוצעה",
              style="success").show()
    self.clear_data()

    
