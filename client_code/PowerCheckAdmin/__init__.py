from ._anvil_designer import PowerCheckAdminTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('PowerCheckAdmin')
class PowerCheckAdmin(PowerCheckAdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.add_engine.visible = True
    self.remove_engine.visible = True
    self.user_management.visible = True
    # Any code you write here will run before the form opens.

  def new_test_click(self, **event_args) -> None:
    routing.set_url_hash('NewPowerCheckForm')

  def history_click(self, **event_args):
    routing.set_url_hash('History')

  def add_engine_click(self, **event_args):
    routing.set_url_hash('AddEngine')

  def remove_engine_click(self, **event_args):
    routing.set_url_hash('RemoveEngine')

  def engine_graph_click(self, **event_args):
    routing.set_url_hash('EngineGraph')

  def user_management_click(self, **event_args):
    routing.set_url_hash('UserManagement')
