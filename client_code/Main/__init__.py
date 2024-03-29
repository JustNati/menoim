from ._anvil_designer import MainTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing
from ..AddEngine import AddEngine
from ..NewPowerCheckForm import NewPowerCheckForm
from ..PowerCheck import PowerCheck
from ..RemoveEngine import RemoveEngine
from ..TorqueCalc import TorqueCalc
from ..PowerTestResult import PowerTestResult
from ..EngineGraph import EngineGraph
from ..EngineStartup import EngineStartup
from ..UserManagement import UserManagement
from ..History import History
from ..utils import check_permissions
from ..PowerCheckAdmin import PowerCheckAdmin
from ..AirPowerCheck import AirPowerCheck
from ..NewAirPowerCheck import NewAirPowerCheck
from ..AirHistory import AirHistory

@routing.route('', title='Home')
@routing.main_router
class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)  
    # Any code you write here will run before the form opens.

  def torque_calc_click(self, **event_args) -> None:
    routing.set_url_hash('TorqueCalc')

  def performance_click(self, **event_args):
    if (check_permissions()):
      routing.set_url_hash('PowerCheckAdmin')
    else:
      routing.set_url_hash('PowerCheck')

  def engine_startup_click(self, **event_args):
    routing.set_url_hash('EngineStartup')

  def admin_login_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel=True)

  def link_1_click(self, **event_args):
    if (check_permissions()):
      routing.set_url_hash('PowerCheckAdmin')
    else:
      routing.set_url_hash('PowerCheck')

  def link_2_click(self, **event_args):
   routing.set_url_hash('TorqueCalc')

  def link_3_click(self, **event_args):
    routing.set_url_hash('EngineStartup')

  def link_4_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel=True)

  def link_5_click(self, **event_args):
    if (check_permissions()):
      routing.set_url_hash('AirPowerCheck')
    else:
      routing.set_url_hash('')
      Notification("אין גישה למשתמשים פרט למנהל",
             title="אין גישה",
             style="danger").show()

  def air_performance_click(self, **event_args):
    if (check_permissions()):
      routing.set_url_hash('AirPowerCheck')
    else:
      routing.set_url_hash('')
      Notification("אין גישה למשתמשים פרט למנהל",
             title="אין גישה",
             style="danger").show()
      
