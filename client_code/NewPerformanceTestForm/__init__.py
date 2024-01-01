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
      'is_retest' : self.recheck_btn.checked,
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
  
  def load_engine_data(self):
    """This method is called when the button is clicked"""
    print(self.engine_num_dd.selected_value)
    if self.engine_num_dd.selected_value is None:
      Notification("A message",
             title="A message title",
             style="danger").show()
    else:
      # Engine details
      rows = app_tables.engines.get(engine_num=self.engine_num_dd.selected_value)
      rows_dict = {x[0]:x[1] for x in list(rows)}
      self.tail_num_info_lbl.text = rows_dict['tail_num']
      self.side_info_lbl.text = rows_dict['side']
      day, month, year = rows_dict['assemble_date'].day, rows_dict['assemble_date'].month, rows_dict['assemble_date'].year
      self.assemble_date.text = f'{day}/{month}/{year}'
      self.time_on_asseble.text = rows_dict['time_on_assemble']
      e_type = rows_dict['engine_type']
      self.engine_type_info_lbl.text = f'PT6-A{e_type}'

      # fields init
      self.add_tmp_dd.selected_value = '4'
      
      # users init
      approvers, submitters = [], []
      for r in app_tables.users.search():
        submitters.append(r['name'])
        if r['is_approver']:
          approvers.append(r['name'])
      self.submitter_name_dd.items = submitters
      self.approver_name_dd.items = approvers
      
      
      self.engine_info_panel.visible = True
      self.test_form_panel.visible = True
      

  def update_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.update_test()

  def engine_num_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    self.load_engine_data()
