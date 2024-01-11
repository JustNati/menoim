from ._anvil_designer import EngineGraphTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

@routing.route('EngineGraph')
class EngineGraph(EngineGraphTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #engines = app_tables.powertests. צריך למצוא את רשימת המנועים (גם האלה שמוסרים, כלומר רשימה יחודית)
    # Any code you write here will run before the form opens.
