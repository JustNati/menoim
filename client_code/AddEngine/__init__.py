from ._anvil_designer import AddEngineTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddEngine(AddEngineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    tails = sorted([r['tail_number'] for r in app_tables.tails.search()])
    self.tails = tails
    self.tail_num.items = tails
    # Any code you write here will run before the form opens.
    
  def add_engine_click(self, **event_args):
    """This method is called when the button is clicked"""

    if (self.engine_num.text is None or
          self.engine_side.selected_value is None or
          self.engine_type.text is None or
          self.tail_num.selected_value is None or
          self.assembly_date.date is None or
          self.start_hours.text is None):
      Notification("נא למלא את כל השדות",
             title="חסרים נתונים",
             style="danger").show()
    elif (len(app_tables.engines.search(tail_num=self.tail_num.selected_value, side=self.engine_side.selected_value)) > 0):
      Notification("קיים מנוע אחר שמורכב במטוס זה באותו הצד",
             title="מנוע אחר מורכב",
             style="danger").show()
    elif (len(app_tables.engines.search(engine_num=self.engine_num.text))> 0):
      Notification("מנוע זה כבר מורכב על מנוע",
             title="מנוע בשימוש",
             style="danger").show()
    else:   
      newRow = app_tables.engines.add_row(assemble_date=self.assembly_date.date,
                                          engine_num=self.engine_num.text,
                                          engine_type=self.engine_type.text,
                                        time_on_assemble=self.start_hours.text,
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



