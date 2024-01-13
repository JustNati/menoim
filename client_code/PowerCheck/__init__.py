from ._anvil_designer import PowerCheckTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('PowerCheck')
class PowerCheck(PowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    logged_user = anvil.users.get_user()
    if (logged_user['is_moderator'] is False or logged_user['is_moderator'] is None):
      self.add_engine.visible = False
      self.remove_engine.visible = False
      self.user_management.visible = False
    else:
      self.add_engine.visible = True
      self.remove_engine.visible = True
      self.user_management.visible = True
    # Any code you write here will run before the form opens.

  def new_test_click(self, **event_args) -> None:
    '''
    move to ne
    '''
    #open_form('NewPowerCheckForm')
    routing.set_url_hash('NewPowerCheckForm')

  def report_by_tail_click(self, **event_args):
    """This method is called when the button is clicked"""
    #open_form('ChecksHistoryByTail')
    routing.set_url_hash('ChecksHistoryByTail')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #open_form('ChecksHistoryByEngine')
    routing.set_url_hash('ChecksHistoryByEngine')

  def explore_records_click(self, **event_args):
    """This method is called when the button is clicked"""
    #open_form('TestsHistory')
    routing.set_url_hash('TestsHistory')

  def add_engine_click(self, **event_args):
    """This method is called when the button is clicked"""
    #open_form('AddEngine')
    routing.set_url_hash('AddEngine')

  def remove_engine_click(self, **event_args):
    """This method is called when the button is clicked"""
    #open_form('RemoveEngine')
    routing.set_url_hash('RemoveEngine')

  def engine_graph_click(self, **event_args):
    """This method is called when the button is clicked"""
    routing.set_url_hash('EngineGraph')

  def user_management_click(self, **event_args):
    """This method is called when the button is clicked"""
    routing.set_url_hash('UserManagement')



