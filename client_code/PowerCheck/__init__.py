from ._anvil_designer import PowerCheckTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PowerCheck(PowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    logged_user = anvil.users.get_user()
    if (logged_user['is_moderator'] is False):
      self.add_engine.visible = False
      self.remove_engine.visible = False
    else:
      self.add_engine.visible = True
      self.remove_engine.visible = True
    # Any code you write here will run before the form opens.

  def new_test_click(self, **event_args) -> None:
    '''
    move to ne
    '''
    open_form('NewPowerCheckForm')

  def report_by_tail_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ChecksHistoryByTail')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ChecksHistoryByEngine')

  def explore_records_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('TestsHistory')



