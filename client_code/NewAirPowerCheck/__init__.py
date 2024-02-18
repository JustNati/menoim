from ._anvil_designer import NewAirPowerCheckTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
from datetime import datetime, date

@routing.route('NewAirPowerCheck')
class NewAirPowerCheck(NewAirPowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    today = datetime.now()
    self.tail_num_dd.items = sorted([r['tail_number'] for r in app_tables.tails.search()])
    self.date.date = f"{today.day}/{today.month}/{today.year}"
    prev_ref = app_tables.airpowertests.search(tables.order_by('reference', ascending=False))[0]['reference']
    self.ref_txt.text = prev_ref + 1
    # Any code you write here will run before the form opens.


  def clear_data(self):
    self.tail_num_dd.selected_value = None
    self.date.date = None
    self.pilot_name.text = None
    self.outside_temp.text = None
    self.speed.text = None
    self.torque.text = None
    self.engine_temp.text = None
    self.n1_rpm.text = None
    self.ref_txt = None
    
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
      if (self.engine_temp.text > 800):
        Notification("טמפ' המנוע לא במגבלות",
             title="בדיקה לא שמישה",
             style="danger").show()
        self.engine_temp.foreground = 'red'
      else:
        self.engine_temp.foreground = 'black'
      if (self.n1_rpm.text > 101.5):
        Notification('סל"ד לא במגבלות',
             title="בדיקה לא שמישה",
             style="danger").show()
        self.n1_rpm.foreground = 'red'
      else:
        self.n1_rpm.foreground = 'black'
      if (self.n1_rpm.foreground == 'black' and self.engine_temp.foreground == 'black'):
        Notification('כלל הנתונים עומדים במגבלות',
             title="בדיקה שמישה",
             style="success").show()
      # Need to add checking to data, and add the record to the data base
      # also need to create copy of history to this history, also only accessable by admin

  def button_1_click(self, **event_args):
    if (self.check_all_fields() is False):
      Notification("נא למלא את כל השדות הרלוונטים",
             title="חסר נתונים",
             style="danger").show()
    else:
      last_ref = app_tables.airpowertests.search(tables.order_by('reference', ascending=False))[0]['reference']
      new_record = {
        'tail_num': self.tail_num_dd.selected_value,
        'date': self.date.date,
        'pilot_name': self.pilot_name.text,
        'outside_temp': self.outside_temp.text,
        'speed': self.speed.text,
        'torque': self.torque.text,
        'engine_temp': self.engine_temp.text,
        'n1_rpm': self.n1_rpm.text,
        'reference': last_ref+1
      }
      app_tables.airpowertests.add_row(**new_record)
      self.clear_data()
      notif_text = f"הבדיקה התווספה למסד הנתונים, סימוכין: {last_ref+1}"
      Notification(notif_text,
             title="עדכון בוצע בהצלחה",
             style="success").show()
