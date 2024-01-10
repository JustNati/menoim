from ._anvil_designer import NewPowerCheckFormTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, date
from ..utils import *
from .. import config# import *
from ..PowerTestResult import PowerTestResult
# TODO: tail list

class NewPowerCheckForm(NewPowerCheckFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    today = datetime.now()
    self.test_date.date = f"{today.day}/{today.month}/{today.year}"
    a = [x['name'] for x in app_tables.powertests.list_columns()]
    engines = sorted([r['engine_num'] for r in app_tables.engines.search()])
    self.engine_num_dd.items = engines
    self.origin_assemble_date = None
  
  def clear_data(self):
    open_form('NewPowerCheckForm')
    
  def update_test(self):
    last_ref = app_tables.powertests.search(tables.order_by('reference', ascending=False))[0]['reference']
    
    new_record = {
      'reference' : last_ref+1,
      'engine_num' : self.engine_num_dd.selected_value,
      'tail' : self.tail_num_info_lbl.text,
      'side' : self.side_info_lbl.text,
      'assmble_date' : self.origin_assemble_date,
      'assmble_eng_hours' : float(self.time_on_asseble.text),
      'test_date' : self.test_date.date,
      'is_retest' : self.recheck_btn.checked,
      'cur_engine_hours' : self.engine_time.text,
      'max_env_temp_OAT' : float(self.env_final_tmp_lbl.text.split(': ')[1]),
      'barometric_pressure' : self.barometric_pressure_txt.text,
      'engine_torque' : self.engine_torque_txt.text,
      'test_n1_rpm' : self.n1_rpm_txt.text,
      'test_itt' : self.out_itt_ff_temp_txt.text,
      'test_wf' : self.out_wf_ff_txt.text,
      'test_notes' : self.notes_area.text
    }

    is_valid_record = validate_empty_values(new_record, config.default_values, exclude_list=['test_notes'])
    if not is_valid_record or self.engine_num_dd.selected_value is None:
      Notification("נא למלא את כל השדות הרלוונטים",
             title="חסר נתונים",
             style="danger").show()
    else:
      res_modal = PowerTestResult(new_record['test_n1_rpm'], new_record['test_itt'], 
                                  new_record['test_wf'], new_record['barometric_pressure'],)
      alert(res_modal, large=True, dismissible=False, buttons=[])
      if res_modal.updated:
        res_record = {
          'n1_diff': float(res_modal.n1_res.text),
          'itt_diff': float(res_modal.itt_res.text),
          'wf_ff_diff': float(res_modal.wf_ff_res.text),
          'submitter': res_modal.submitter_name_dd.selected_value,
          'approver': res_modal.approver_name_dd.selected_value,
          'test_result': res_modal.usability_dd.selected_value
        }
        new_record.update(res_record)
        app_tables.powertests.add_row(**new_record)
        self.clear_data()
        Notification("!הנתונים נשמרו בהצלחה",
             title="נתונים נשמרו",
             style="success").show()
      
  def load_engine_data(self):
    """This method is called when the button is clicked"""
    if self.engine_num_dd.selected_value is None:
      Notification("נא לבחור מספר מנוע",
             title="מספר מנוע לא תקין",
             style="warning").show()
    else:
      # Engine details
      rows = app_tables.engines.get(engine_num=self.engine_num_dd.selected_value)
      rows_dict = {x[0]:x[1] for x in list(rows)}
      self.tail_num_info_lbl.text = rows_dict['tail_num']
      self.side_info_lbl.text = rows_dict['side']
      self.origin_assemble_date = rows_dict['assemble_date']
      day, month, year = rows_dict['assemble_date'].day, rows_dict['assemble_date'].month, rows_dict['assemble_date'].year
      self.assemble_date.text = f'{day}/{month}/{year}'
      self.time_on_asseble.text = rows_dict['time_on_assemble']
      e_type = rows_dict['engine_type']
      self.engine_type_info_lbl.text = f'PT6-A{e_type}'

      # fields init
      self.engine_info_panel.visible = True
      self.test_form_panel.visible = True
      
  def update_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.update_test()

  def engine_num_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    self.load_engine_data()

  def max_env_tmp_txt_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    final_tmp = 0
    if self.max_env_tmp_txt.text != '' and not self.max_env_tmp_txt.text is None:
      final_tmp = float(self.max_env_tmp_txt.text) + config.temperature_addition_factor
    self.env_final_tmp_lbl.text = f"טמפ' הסביבה המדווחת(+{config.temperature_addition_factor}): {final_tmp}"

  # ---------------------------------------------
  # ----------------- Validation ----------------

