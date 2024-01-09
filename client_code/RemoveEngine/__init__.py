from ._anvil_designer import RemoveEngineTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RemoveEngine(RemoveEngineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engines_dd.items = engines
    # Any code you write here will run before the form opens.

  def remove_engine_click(self, **event_args):
    """This method is called when the button is clicked"""
    engine_to_remove = app_tables.engines.get(engine_num=self.engines_dd.selected_value)
    change_tail = app_tables.tails.get(tail_number=engine_to_remove['tail_num'])
    if (engine_to_remove['side'] == 'right'):
      change_tail['right_engine_num'] = "-1"
    else:
      change_tail['left_engine_num'] = "-1"
    engine_to_remove.delete()
    Notification("!מנוע הוסר בהצלחה",
             title="הוסרה הצליחה",
             style="success").show()
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engines_dd.items = engines
    
