from ._anvil_designer import ChecksHistoryByEngineTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ChecksHistoryByEngine(ChecksHistoryByEngineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engine_num_dd.items = engines

    # Any code you write here will run before the form opens.

  def load_engine_data(self):
    """This method is called when the button is clicked"""
    if self.engine_num_dd.selected_value is None:
      Notification("נא לבחור מספר מנוע",
             title="מספר מנוע לא תקין",
             style="warning").show()
      return
    self.main_data_grid.visible = True
    self.main_data_grid.items = anvil.server.call('get_powertests')

  def engine_num_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    self.load_engine_data()