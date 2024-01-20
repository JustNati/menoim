from ._anvil_designer import EngineStartupResultTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('EngineStartupResult')
class EngineStartupResult(EngineStartupResultTemplate):
  def __init__(self, right_magneto, left_magneto, manifold_press, max_ff, cht_max, max_oil_press, oil_temp, min_oil_press, cht_min, mixture_dilute, metered_ffp_min, unmetered_ffp_min, max_rpm, metered_ffp_max, unmetered_ffp_max, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = right_magneto
    self.label_2.text = left_magneto
    self.label_11.text = manifold_press
    self.label_12.text = max_ff
    self.label_13.text = cht_max
    self.label_14.text = max_oil_press
    self.label_15.text = oil_temp
    self.label_16.text = min_oil_press
    self.label_17.text = cht_min
    self.label_18.text = mixture_dilute
    self.label_25.text = metered_ffp_min
    self.label_26.text = unmetered_ffp_min
    self.label_22.text = max_rpm
    self.label_23.text=  metered_ffp_max
    self.label_24.text = unmetered_ffp_max
    # Any code you write here will run before the form opens.
