from ._anvil_designer import NewPerformanceTestFormTemplate
from anvil import *
from datetime import datetime
# TODO: tail list

class NewPerformanceTestForm(NewPerformanceTestFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    today = datetime.now()
    self.test_date.date = f"{today.day}/{today.month}/{today.year}"

  def load_engine_data_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.engine_info_panel.visible = True
    self.test_form_panel.visible = True
