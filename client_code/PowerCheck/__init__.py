from ._anvil_designer import PowerCheckTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('PowerCheck')
class PowerCheck(PowerCheckTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def new_test_click(self, **event_args) -> None:
    routing.set_url_hash('NewPowerCheckForm')

  def history_click(self, **event_args):
    routing.set_url_hash('History')

  def engine_graph_click(self, **event_args):
    routing.set_url_hash('EngineGraph')

  def link_1_click(self, **event_args):
    routing.set_url_hash('NewPowerCheckForm')

  def link_2_click(self, **event_args):
    routing.set_url_hash('History')

  def link_3_click(self, **event_args):
    routing.set_url_hash('EngineGraph')


