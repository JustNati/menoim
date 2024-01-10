from ._anvil_designer import TorqueCalcTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TorqueCalc(TorqueCalcTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def calc_torque(self, **event_args):
    # בודק שהמשתמש הכניס את כל הנתונים 
    if (self.extention_len.text is None or self.desired_torque.text == None or self.torque_len.text == None): 
      self.final_result.visible = False
      return False
    # אם כל הנתונים הוכנסו
    else: 
      self.final_result.text = round((self.desired_torque.text * self.torque_len.text) / (self.torque_len.text + self.extention_len.text),2) # נוסחה לחישוב ערך טורק
      self.final_result.visible = True 
    # Any code you write here will run before the form opens.
