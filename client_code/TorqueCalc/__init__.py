from ._anvil_designer import TorqueCalcTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TorqueCalc(TorqueCalcTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def calc_torque(self, **event_args):
    if (self.extention_len.text is None or self.desired_torque.text == None or self.torque_len.text == None): #בודק שהמשתמש הכניס את כל הנתונים
      self.final_result.visible = False
      return False
    else: # אם כל הנתונים הוכנסו
      self.final_result.text = (self.desired_torque.text * self.torque_len.text) / (self.torque_len.text + self.extention_len.text) # נוסחה לחישוב ערך טורק
      self.final_result.visible = True 
    # Any code you write here will run before the form opens.