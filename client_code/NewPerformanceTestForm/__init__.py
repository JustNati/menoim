from ._anvil_designer import NewPerformanceTestFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
from ..utils import *
# TODO: tail list

class NewPerformanceTestForm(NewPerformanceTestFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    today = datetime.now()
    self.test_date.date = f"{today.day}/{today.month}/{today.year}"
    a = [x['name'] for x in app_tables.powertests.list_columns()]
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engine_num_dd.items = engines
 
  def update_test(self):
    last_ref = app_tables.powertests.search(tables.order_by('reference', ascending=False))[0]['reference']
    default_values = ['',None]
    #['','בחרו מנוע','בחרו מזין נתונים', 'בחרו מאשר נתונים', 'בחרו שמישות']
    new_record = {
      'reference' : last_ref+1,
      'engine_num' : self.engine_num_dd.selected_value,
      'tail' : self.tail_num_info_lbl.text,
      'side' : self.side_info_lbl.text,
      'assmble_data' : self.assemble_date.text,
      'assmble_eng_hours' : self.time_on_asseble.text,
      'test_date' : self.test_date.date,
      'cur_engine_hours' : self.engine_time.text,
      'max_env_temp_OAT' : self.max_env_tmp_txt.text,
      'barometric_pressure' : self.barometric_pressure_txt.text,
      'engine_torque' : self.engine_torque_txt.text,
      'test_n1_rpm' : self.n1_rpm_txt.text,
      'test_itt' : self.out_itt_ff_temp_txt.text,
      'test_wf' : self.out_wf_ff_txt.text,
      'required_wf' : self.required_wf_ff_txt.text,
      'test_notes' : self.notes_area.text,
      'submitter' : self.submitter_name_dd.selected_value,
      'approver' : self.approver_name_dd.selected_value,
      'test_result' : self.usability_dd.selected_value
    }

    is_valid_record = validate_empty_values(new_record, default_values)
    if not is_valid_record or self.engine_num_dd.selected_value is None:
      Notification("A message",
             title="A message title",
             style="danger").show()
  
  def load_engine_data_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(self.engine_num_dd.selected_value)
    if self.engine_num_dd.selected_value is None:
      Notification("A message",
             title="A message title",
             style="danger").show()
    else:
      self.engine_info_panel.visible = True
      self.test_form_panel.visible = True

  def update_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.update_test()
