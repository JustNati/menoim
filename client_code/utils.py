import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
def find_nearest_value(arr: list, target: float):
    closest_value = arr[0]  # Initialize with the first value in the array
    min_difference = abs(target - closest_value)  # Initialize the minimum difference

    for value in arr:
        difference = abs(target - value)
        if difference < min_difference:
            min_difference = difference
            closest_value = value

    return closest_value
  
def calc_ng(x: float) -> tuple:
  m = 0.147 if x<44 else 0.04
  c = 95.1 if x<44 else 101.4
  return round(m*x + c,2)

def calc_itt(x: float) -> tuple:
  m = 3 if x<43.5 else 2
  c = 653 if x<43.5 else 694
  return round(m*x + c,2)

def validate_empty_values(dictionary, values_list, exclude_list=[]):
    # Check if any values in the dictionary are empty or match any value in the list
    for k, val in dictionary.items():
      if k in exclude_list: continue # exclude from check
      if val in values_list:
        return False
    return True

def calc_barometric_pressure(x: float, barometric_pressure_val: float,
                            barometric_vaues = [24,26,28,29.97,31]) -> tuple:
  m = 0.17 if x<44 else -3
  c = 0
  barometric_val = find_nearest_value(barometric_vaues, barometric_pressure_val)                          
  if barometric_val == 24:
    c = 427.5 if x<44 else 565
  elif barometric_val == 26:
    c = 462.5 if x<44 else 575
  elif barometric_val == 28:
    c = 502.5 if x<44 else 635
  elif barometric_val == 29.97:
    c = 532.5 if x<44 else 670
  elif barometric_val == 31:
    c = 547.5 if x<44 else 690
  return m*x + c

def search_engines_with_query_for_tail(query):
  result = app_tables.powertests.search(tables.order_by("reference", ascending=False))
  finished_results = []
  if query:
    result = [
      row for row in result
        if query in str(row['engine_num'])
        or query in str(row['side'])
        or query in str(row['test_date'].strftime("%d/%m/%Y"))
        or query in str(row['cur_engine_hours'])
        or query in str(row['n1_diff'])
        or query in str(row['itt_diff'])
        or query in str(row['wf_ff_diff'])
        or query in str(row['reference'])
        or query in str(row['test_notes'])
    ]
  for r in result:
    new_row = {
          'engine_num': r['engine_num'],
          'side': r['side'],
          'test_date': r['test_date'].strftime("%d/%m/%Y"),
          'engine_hours': r['cur_engine_hours'],
          'rpm_diff': r['n1_diff'],
          'temp_diff': r['itt_diff'],
          'ff_diff': r['wf_ff_diff'],
          'reference': r['reference'],
          'comments': r['test_notes'] 
    }
    finished_results.append(new_row)
  return finished_results

def check_permissions():
  logged_user = anvil.users.get_user()
  if (logged_user is None):
    return False
  if (logged_user['is_moderator'] is not None and logged_user is not False):
    return True
  return False

def search_air_tests(query):
  result = app_tables.airpowertests.search(tables.order_by("reference", ascending=False))
  finished_results = []
  if query:
    result = [
      row for row in result
        if query in str(row['reference'])
        or query in str(row['date'].strftime("%d/%m/%Y"))
        or query in str(row['pilot_name'])
        or query in str(row['outside_temp'])
        or query in str(row['speed'])
        or query in str(row['torque'])
        or query in str(row['engine_temp'])
        or query in str(row['n1_rpm'])
    ]
  for r in result:
    new_row = {
          'reference': r['reference'],
          'date': r['date'].strftime("%d/%m/%Y"),
          'pilot_name': r['pilot_name'],
          'outside_temp': r['outside_temp'],
          'speed': r['speed'],
          'torque': r['torque'],
          'engine_temp': r['engine_temp'],
          'n1_rpm': r['n1_rpm'] 
    }
    finished_results.append(new_row)
  return finished_results