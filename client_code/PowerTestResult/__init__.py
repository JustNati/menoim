from ._anvil_designer import PowerTestResultTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..utils import *
from .. import config

class PowerTestResult(PowerTestResultTemplate):
  def __init__(self, recorded_n1, recorded_itt, recorded_ff, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.updated = False
    self.n1_res.text = calc_ng(recorded_n1)
    self.itt_res.text = calc_itt(recorded_itt)
    self.wf_ff_res.text = calc_barometric_pressure(recorded_ff, )

    # users init
    approvers, submitters = [], []
    for r in app_tables.users.search():
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
      style="danger").show()
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
