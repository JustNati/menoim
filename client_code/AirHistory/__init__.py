from ._anvil_designer import AirHistoryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
from ..utils import *

@routing.route('AirHistory')
class AirHistory(AirHistoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.main_data_grid.role = 'wide'
    tails = sorted([r['tail_number'] for r in app_tables.tails.search()])
    self.tail_num_dd.items = tails
    self.query = None
    self.loaded_data = None
    self.order = False
    self.load_initial_engine_data()
    #self.repeating_panel_1.items = app_tables.people.search(tables.order_by('age'))

    # Any code you write here will run before the form opens.

  def load_initial_engine_data(self):
    rows = None
    if (self.query == 'tail'):
      rows = app_tables.airpowertests.search(tables.order_by("reference", ascending=False), tail= self.tail_num_dd.selected_value)
    else:
      rows = app_tables.airpowertests.search(tables.order_by("reference", ascending=False))
    finsihed_rows = []
    for r in rows:
      finsihed_rows.append({
        'reference': r['reference'],
        'date': r['date'].strftime("%d/%m/%Y"),
        'pilot_name': r['pilot_name'],
        'outside_temp': r['outside_temp'],
        'speed': r['speed'],
        'torque': r['torque'],
        'engine_temp': r['engine_temp'],
        'n1_rpm': r['n1_rpm']
      })
    self.repeating_panel_data.items = finsihed_rows
    self.loaded_data = finsihed_rows

  def update_order(self, query):
    new_engines_order = sorted(self.loaded_data, key=lambda d: d[query])
    if (self.order is False):
      new_engines_order.reverse()
    self.repeating_panel_data.items = new_engines_order

  def send_query_click(self, **event_args):
    air_tests = search_air_tests(self.search_query.text)
    self.tail_num_dd.selected_value = None
    self.loaded_data = air_tests
    self.repeating_panel_data.items = air_tests
    self.reset_icons()

  def tail_num_dd_change(self, **event_args):
    self.query = 'tail'
    self.load_initial_engine_data()

  def reference_click(self, **event_args):
    self.query='reference'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.reference.icon = 'fa:sort-alpha-asc'
    else:
      self.reference.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)

  def date_click(self, **event_args):
    self.query='date'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.date.icon = 'fa:sort-alpha-asc'
    else:
      self.date.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)

  def pilot_name_click(self, **event_args):
    self.query='pilot_name'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.pilot_name.icon = 'fa:sort-alpha-asc'
    else:
      self.pilot_name.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)
    
  def reset_icons(self):
    self.outside_temp.icon = None
    self.date.icon = None
    self.pilot_name.icon = None  
    self.reference.icon = None
    self.speed.icon = None
    self.torque.icon = None
    self.n1_rpm.icon = None
    self.engine_temp.icon = None

  def outside_temp_click(self, **event_args):
    self.query='outside_temp'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.outside_temp.icon = 'fa:sort-alpha-asc'
    else:
      self.outside_temp.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)

  def speed_click(self, **event_args):
    self.query='speed'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.speed.icon = 'fa:sort-alpha-asc'
    else:
      self.speed.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)

  def torque_click(self, **event_args):
    self.query='torque'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.torque.icon = 'fa:sort-alpha-asc'
    else:
      self.torque.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)

  def engine_temp_click(self, **event_args):
    self.query='engine_temp'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.engine_temp.icon = 'fa:sort-alpha-asc'
    else:
      self.engine_temp.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)

  def n1_rpm_click(self, **event_args):
    self.query='n1_rpm'
    self.order = not self.order
    self.reset_icons()
    if (self.order):
      self.n1_rpm.icon = 'fa:sort-alpha-asc'
    else:
      self.n1_rpm.icon = 'fa:sort-alpha-desc'
    self.update_order(self.query)
