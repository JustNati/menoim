from ._anvil_designer import PowerCheckTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PowerCheck(PowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def new_test_click(self, **event_args) -> None:
    '''
    move to ne
    '''
    open_form('NewPowerCheckForm')
