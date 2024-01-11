from ._anvil_designer import ChecksHistoryByEngineTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('ChecksHistoryByEngine')
class ChecksHistoryByEngine(ChecksHistoryByEngineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engine_num_dd.items = engines
    self.main_data_grid.role = 'wide'
    self.main_data_grid.columns[0]['width'] = 500
    # Any code you write here will run before the form opens.

  def load_engine_data(self):
    """This method is called when the button is clicked"""
    if self.engine_num_dd.selected_value is None:
      Notification("נא לבחור מספר מנוע",
             title="מספר מנוע לא תקין",
             style="warning").show()
      return
    else:
      # Quering the database for engine num rows
      rows = app_tables.powertests.search(engine_num=self.engine_num_dd.selected_value)
      finished_rows = []
      # For every row i create a new presentable and organized list
      for r in rows:
        new_row = {
          'test_date': r['test_date'],
          'engine_hours': r['cur_engine_hours'],
          'rpm_diff': r['n1_diff'],
          'temp_diff': r['itt_diff'],
          'ff_diff': r['wf_ff_diff'],
          'reference': r['reference'],
          'comments': r['test_notes']
        }
        finished_rows.append(new_row)
      #test_date = [r['test_date'] for r in rows]
      # Appending the finished list to the visual table
      self.repeating_panel_1.items = finished_rows
      self.main_data_grid.visible = True
  
      
      

  def engine_num_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    self.load_engine_data()