from ._anvil_designer import PowerTestResultTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..utils import *
from .. import config
from anvil_extras import routing

@routing.route('PowerTestResult')
class PowerTestResult(PowerTestResultTemplate):
  def __init__(self, recorded_n1, recorded_itt, max_temp, recorded_ff, barometric_pressure, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.updated = False
    self.n1_res.text = round(recorded_n1 - calc_ng(max_temp),2)
    self.itt_res.text =  round(recorded_itt - calc_itt(max_temp),2) 
    self.wf_ff_res.text = round(calc_barometric_pressure(max_temp, barometric_pressure) - recorded_ff,2)
    # users init
    approvers, submitters = [], []
    for r in app_tables.users.search():
      if(r['name'] is not None):
        submitters.append(r['name'])
        if r['is_approver']:
          approvers.append(r['name'])
    self.submitter_name_dd.items = submitters
    self.approver_name_dd.items = approvers

    # Any code you write here will run before the form opens.
       
  def validate_submitters(self):
    return self.submitter_name_dd.selected_value != self.approver_name_dd.selected_value

  def cancel_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    Notification("!הנתונים לא נשמרו",
      title="שימו לב",
      style="warning").show()
    self.raise_event('x-close-alert')
    
  def update_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    res_record = {
      'submitter': self.submitter_name_dd.selected_value,
      'approver': self.approver_name_dd.selected_value,
      'test_result': self.usability_dd.selected_value
    }
    is_valid_record = validate_empty_values(res_record, config.default_values)
    if not is_valid_record:
      Notification("נא למלא את כל השדות הרלוונטים",
            title="חסר נתונים",
            style="danger").show()
      
    elif not self.validate_submitters():
      Notification("אין לבחור מבצע ובודק זהים",
            title="",
            style="danger").show()
    else:
      self.updated = True
      self.raise_event('x-close-alert')
