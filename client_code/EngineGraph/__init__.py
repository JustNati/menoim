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
    self.selected_engine = self.engines_dd.selected_value
    self.createPlots()

  def createPlots(self):
    power_tests = app_tables.powertests.search(q.all_of(engine_num=self.selected_engine))
    dates, n1_diff, itt_diff, wf_ff_diff = [], [], [], []
    for r in power_tests:
      dates.append(r['test_date'].strftime("%d/%m/%Y"))
      n1_diff.append(r['n1_diff'])
      itt_diff.append(r['itt_diff'])
      wf_ff_diff.append(r['wf_ff_diff'])
      
    self.plot_1.layout = {
      'title': 'N1 Diff / Time',
      'xaxis': {
        'title': 'time'
       },
      'yaxis': {
        'title': 'N1_Diff'
      }
    }
    self.plot_2.layout = {
      'title': 'ITT Diff / Time',
      'xaxis': {
        'title': 'time'
       },
      'yaxis': {
        'title': 'ITT_Diff'
      }
    }
    self.plot_3.layout = {
      'title': 'WF_FF_Diff / Time',
      'xaxis': {
        'title': 'time'
       },
      'yaxis': {
        'title': 'WF_FF_Diff'
      }
    }
    self.plot_1.templates["my_template"] = {"layout": {"plot_bgcolor": "bisque"}}
    self.plot_2.templates["my_template"] = {"layout": {"plot_bgcolor": "bisque"}}
    self.plot_3.templates["my_template"] = {"layout": {"plot_bgcolor": "bisque"}}
    
    self.plot_1.templates.default = "my_template"
    self.plot_2.templates.default = "my_template"
    self.plot_3.templates.default = "my_template"
    
    self.plot_1.data= go.Scatter(x=dates, y=n1_diff)
    self.plot_2.data= go.Scatter(x=dates, y=itt_diff)
    self.plot_3.data= go.Scatter(x=dates, y=wf_ff_diff)
  
    # Any code you write here will run before the form opens.

  def engines_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_engine = self.engines_dd.selected_value
    self.createPlots()
    
