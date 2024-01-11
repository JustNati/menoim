from ._anvil_designer import EngineGraphTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('EngineGraph')
class EngineGraph(EngineGraphTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    engines_list = list({(r['engine_num']) for r in app_tables.powertests.search()})
    self.engines_dd.items = sorted(set(engines_list))
    selected_engine = self.engines_dd.selected_value
    
    #self.plot_1.data= go.scatter(x=)
    #engines = app_tables.powertests. צריך למצוא את רשימת המנועים (גם האלה שמוסרים, כלומר רשימה יחודית)
    # Any code you write here will run before the form opens.
