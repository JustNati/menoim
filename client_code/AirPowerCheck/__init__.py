from ._anvil_designer import AirPowerCheckTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('AirPowerCheck')
class AirPowerCheck(AirPowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    routing.set_url_hash('NewAirPowerCheck')

  def button_2_click(self, **event_args):
    routing.set_url_hash('AirHistory')
