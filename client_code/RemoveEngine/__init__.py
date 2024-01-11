from ._anvil_designer import RemoveEngineTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('RemoveEngine')
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
    # Checks if user chose engine to remove
    if (engine_to_remove is None):
      Notification("לא נבחר מנוע",
             title="שגיאה, לא ניתן לבצע את הפעולה",
             style="danger").show()
    # If he did choose, remove from the database the engine and change the 
    # engine num in the tails database to '-1' (arbitrary number)
    else:
      change_tail = app_tables.tails.get(tail_number=engine_to_remove['tail_num'])
      if (engine_to_remove['side'] == 'right'):
        change_tail['right_engine_num'] = "-1"
      else:
        change_tail['left_engine_num'] = "-1"
      engine_to_remove.delete()
      Notification("!מנוע הוסר בהצלחה",
              title="הוסרה הצליחה",
              style="success").show()
      # Update the list after user removes engine so he wont remove the same engine by mistake
      engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
      self.engines_dd.items = engines
    
