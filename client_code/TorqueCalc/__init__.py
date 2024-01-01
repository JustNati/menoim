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
    self.final_result.text = (self.desired_torque * self.torque_len) / (self.torque_len + self.extention_len)
    self.final_result.visible = true
    # Any code you write here will run before the form opens.
