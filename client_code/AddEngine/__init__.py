from ._anvil_designer import AddEngineTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('AddEngine')
class AddEngine(AddEngineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    tails = sorted([r['tail_number'] for r in app_tables.tails.search(q.any_of(left_engine_num='-1', right_engine_num='-1'))])
    self.tails = tails
    self.tail_num.items = tails
    # Any code you write here will run before the form opens.
    
  def add_engine_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Check if All the fields are filled
    if (self.engine_num.text is None or
          self.engine_side.selected_value is None or
          self.tail_num.selected_value is None):
      Notification("נא למלא את כל השדות",
             title="חסרים נתונים",
             style="danger").show()
    # Check if there are more than 0 engines on that specific tail & side
    elif (len(app_tables.engines.search(tail_num=self.tail_num.selected_value, side=self.engine_side.selected_value)) > 0):
      Notification("קיים מנוע אחר שמורכב באותו המקום",
             title="מנוע אחר מורכב",
             style="danger").show()
    # Check if that engine is already in the database (which means it already exists)
    elif (len(app_tables.engines.search(engine_num=self.engine_num.text))> 0):
      Notification("מנוע זה כבר מורכב",
             title="מנוע בשימוש",
             style="danger").show()
    # If the engine is not in the database, and the place in the plane is empty,
    # create new engine in the database and change the engine number in the tails database
    else:   
      newRow = app_tables.engines.add_row(engine_num=self.engine_num.text,                              
                                        side=self.engine_side.selected_value,
                                        tail_num=self.tail_num.selected_value)
      if (self.engine_side.selected_value == 'right'):
        changed_tail = app_tables.tails.get(tail_number=self.tail_num.selected_value)
        changed_tail['right_engine_num'] = self.engine_num.text
      else:
        changed_tail = app_tables.tails.get(tail_number=self.tail_num.selected_value)
        changed_tail['left_engine_num'] = self.engine_num.text
      Notification("!מנוע הותקן בהצלחה",
             title="הוספה הצליחה",
             style="success").show()



