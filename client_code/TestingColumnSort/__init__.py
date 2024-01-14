from ._anvil_designer import TestingColumnSortTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TestingColumnSort(TestingColumnSortTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_engine_data()
    # Any code you write here will run before the form opens.

  def load_engine_data(self):
    rows = app_tables.powertests.search(tables.order_by("reference", ascending=False))
    everything, engine_nums, sides, test_dates, engine_hours, rpm_diffs, temp_diffs, ff_diffs, references, comments = [], [] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] 
    for r in rows:
      engine_nums.append({'engine_num':r['engine_num']})
      sides.append(r['side'])
      test_dates.append(r['test_date'].strftime("%d/%m/%Y"))
      everything.append({
        'engine_nu'
      })
    self.repeating_panel_engine_num.items = engine_nums
    self.repeating_panel_sides.items = sides
    self.repeating_panel_test_date.items = test_dates
    self.repeating_panel_engine_num.items = ['1','2','3']
    self.repeating_panel_engine_num.items = [{'1'},{'2'},'3']
    