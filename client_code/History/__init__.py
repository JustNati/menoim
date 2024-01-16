from ._anvil_designer import HistoryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
from ..utils import *

@routing.route('History')
class History(HistoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.main_data_grid.role = 'wide'
    tails = sorted([r['tail_number'] for r in app_tables.tails.search()])
    engines = list(set([r['engine_num'] for r in app_tables.powertests.search(tables.order_by('engine_num'))]))
    self.engine_num_dd.items = engines
    self.tail_num_dd.items = tails
    self.query = None
    self.loaded_data = None
    self.order = False
    self.load_initial_engine_data()
    #self.repeating_panel_1.items = app_tables.people.search(tables.order_by('age'))
    
    # Any code you write here will run before the form opens.

  def load_initial_engine_data(self):
    rows = None
    if (self.query == 'engine'):
      rows = app_tables.powertests.search(tables.order_by("reference", ascending=False), engine_num= self.engine_num_dd.selected_value)
    elif (self.query == 'tail'):
      rows = app_tables.powertests.search(tables.order_by("reference", ascending=False), tail= self.tail_num_dd.selected_value)
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
    self.loaded_data = finsihed_rows

  def update_order(self, query):
    new_engines_order = sorted(self.loaded_data, key=lambda d: d[query]) 
    if (self.order is False):
      new_engines_order.reverse()
    self.repeating_panel_data.items = new_engines_order
  
  def send_query_click(self, **event_args):
    """This method is called when the button is clicked"""
    returned_engines = search_engines_with_query_for_tail(self.search_query.text)
    self.tail_num_dd.selected_value = None
    self.engine_num_dd.selected_value = None
    self.loaded_data = returned_engines
    self.repeating_panel_data.items = returned_engines

  def engine_num_dd_change(self, **event_args):
    self.query = 'engine'
    self.tail_num_dd.selected_value = None
    self.load_initial_engine_data()

  def tail_num_dd_change(self, **event_args):
    self.query = 'tail'
    self.engine_num_dd.selected_value = None
    self.load_initial_engine_data()

  def reference_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='reference'
    self.order = not self.order 
    self.update_order(self.query)

  def comments_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='comments'
    self.order = not self.order
    self.update_order(self.query)

  def ff_diff_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='ff_diff'
    self.order = not self.order
    self.update_order(self.query)

  def temp_diff_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='temp_diff'
    self.order = not self.order
    self.update_order(self.query)

  def rpm_diff_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='rpm_diff'
    self.order = not self.order
    self.update_order(self.query)

  def engine_hours_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='engine_hours'
    self.order = not self.order
    self.update_order(self.query)

  def date_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='date'
    self.order = not self.order
    self.update_order(self.query)

  def side_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='side'
    self.order = not self.order
    self.update_order(self.query)

  def engine_num_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.query='engine_num'
    self.order = not self.order
    self.update_order(self.query)
    
    
    
    
    