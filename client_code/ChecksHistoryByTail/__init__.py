from ._anvil_designer import ChecksHistoryByTailTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ChecksHistoryByTail(ChecksHistoryByTailTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    tails = sorted([r['tail_number'] for r in app_tables.tails.search()])
    self.tail_num_dd.items = tails
    # Any code you write here will run before the form opens.

  def load_engine_data(self):
    """This method is called when the button is clicked"""
    if self.tail_num_dd.selected_value is None:
      Notification("נא לבחור מספר זנב",
             title="מספר זנב לא תקין",
             style="warning").show()
      return
    else:
      # Quering the database for engine num rows
      rows = app_tables.powertests.search(tail=self.tail_num_dd.selected_value)
      finished_rows = []
      # For every row i create a new presentable and organized list
      for r in rows:
        new_row = {
          'engine_num': r['tail'],
          'test_date': r['test_date'],
          'engine_hours': r['cur_engine_hours'],
          'rpm_diff': r['n1_diff'],
          'temp_diff': r['itt_diff'],
          'ff_diff': r['wf_ff_diff'],
          'comments': r['test_notes']
        }
        finished_rows.append(new_row)
      #test_date = [r['test_date'] for r in rows]
      # Appending the finished list to the visual table
      self.repeating_panel_1.items = finished_rows
      self.main_data_grid.visible = True




  def tail_num_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    self.load_engine_data()