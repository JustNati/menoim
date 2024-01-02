from ._anvil_designer import TestsHistoryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TestsHistory(TestsHistoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_tests.items = anvil.server.call('get_powertest')
    self.repeating_panel_tests.role = "horizontal-scroll"