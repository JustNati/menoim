from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def torque_calc_click(self, **event_args) -> None:
    '''
    move to torque calculation page.
    '''
    open_form('TorqueCalc')

  def performance_click(self, **event_args):
    '''
    move to performance test page.
    '''
    open_form('PerformanceTest')
