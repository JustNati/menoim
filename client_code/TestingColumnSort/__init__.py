from ._anvil_designer import TestingColumnSortTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..utils import *

class TestingColumnSort(TestingColumnSortTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.main_data_grid.role = 'wide'
    tails = sorted([r['tail_number'] for r in app_tables.tails.search()])
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engine_num_dd.items = engines
    self.tail_num_dd.items = tails
    self.query = None
    self.load_initial_engine_data()
    # Any code you write here will run before the form opens.

  def load_initial_engine_data(self):
    if (self.query):
      return True
          
    else:
      rows = app_tables.powertests.search(tables.order_by("reference", ascending=False))
    finsihed_rows = []
    for r in rows:
      finsihed_rows.append({
        'engine_num': r['engine_num'],
        'side': r['side'],
        'date': r['test_date'].strftime("%d/%m/%Y"),
        'engine_hours': r['cur_engine_hours'],
        'rpm_diff': r['n1_diff'],
        'temp_diff': r['itt_diff'],
        'ff_diff': r['wf_ff_diff'],
        'reference': r['reference'],
        'comments': r['test_notes']
      })
    self.repeating_panel_data.items = finsihed_rows

  def send_query_click(self, **event_args):
    """This method is called when the button is clicked"""
    returned_engines = search_engines_with_query_for_tail(self.search_query.text)
    self.repeating_panel_data.items = returned_engines

  def engine_num_dd_change(self, **event_args):
    self.query = 'engine'
    

  def tail_num_dd_change(self, **event_args):
    self.query = 'tail'
    
    
    
    