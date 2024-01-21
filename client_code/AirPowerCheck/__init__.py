from ._anvil_designer import AirPowerCheckTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
from datetime import datetime, date

@routing.route('AirPowerCheck')
class AirPowerCheck(AirPowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    today = datetime.now()
    self.tail_num_dd.items = sorted([r['tail_number'] for r in app_tables.tails.search()])
    self.date.date = f"{today.day}/{today.month}/{today.year}"
    # Any code you write here will run before the form opens.

  def check_all_fields(self):
    if (self.tail_num_dd.selected_value is None or self.date.date is None or self.pilot_name is None
        or self.outside_temp.text is None or self.speed.text is None or self.torque.text is None 
        or self.engine_temp.text is None or self.n1_rpm.text is None):
      return False
    else:
      return True
      

  def update_btn_click(self, **event_args):
    if (self.check_all_fields() is False):
      Notification("נא למלא את כל השדות הרלוונטים",
             title="חסר נתונים",
             style="danger").show()
    else:
      new_record = {
        'tail_num': self.tail_num_dd.selected_value,
        'date': self.date.date,
        'pilot_name': self.pilot_name.text,
        'outside_temp': self.outside_temp.text,
        'speed': self.speed.text,
        'torque': self.torque.text,
        'engine_temp': self.engine_temp.text,
        'n1_rpm': self.n1_rpm.text
      }
      # Need to add checking to data, and add the record to the data base
      # also need to create copy of history to this history, also only accessable by admin
      
