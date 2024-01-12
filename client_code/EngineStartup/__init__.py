from ._anvil_designer import EngineStartupTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil_extras import routing

@routing.route('EngineStartup')
class EngineStartup(EngineStartupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def validate_data(self):
    all_the_data = [self.right_magneto.text, self.left_magneto.text, 
                   self.manifold_press.text,
                   self.max_ff.text, self.cht_max.text, self.max_oil_press.text,
                   self.oil_temp.text,
                   self.metered_ffp_min.text, self.unmetered_ffp_min.text, 
                   self.metered_ffp_max.text,
                   self.unmetered_ffp_max.text, self.max_rpm.text]
    for field in all_the_data:
      if(field is None):
        return False
    return True
    
  def check_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (self.validate_data() is False):
      Notification("נא למלא את כל השדות הרלוונטים",
             title="חסר נתונים",
             style="danger").show()
    else:
      isAcceptable = True

      ##1700 RPM Check list
      if (self.left_magneto.text > 150 or self.left_magneto.text < 0):
        self.left_magneto.foreground= 'red'
        isAcceptable = False
      else:
        self.left_magneto.foreground = 'black'
      if (self.right_magneto.text > 150 or self.right_magneto.text < 0):
        self.right_magneto.foreground= 'red'
        isAcceptable = False
      else:
        self.right_magneto.foreground = 'black'
      if (abs(self.right_magneto.text - self.left_magneto.text) > 50):
        self.right_magneto.foreground= 'red'
        self.left_magneto.foreground= 'red'
        isAcceptable = False
      

      # 2700 RPM Check list
      if (self.manifold_press.text > 29.6 or self.manifold_press.text < 0):
        self.manifold_press.foreground = 'red'
        isAcceptable = False
      else:
        self.manifold_press.foreground = 'black'
      if (self.max_ff.text > 26.4 or self.max_ff.text < 25):
        self.max_ff.foreground = 'red'
        isAcceptable = False
      else:
        self.max_ff.foreground = 'black'
      if (self.cht_max.text > 238 or self.cht_max.text < 0):
        self.cht_max.foreground = 'red'
        isAcceptable = False
      else:
        self.cht_max.foreground = 'black'
      if (self.max_oil_press.text > 60 or self.max_oil_press.text < 10):
        self.max_oil_press.foreground = 'red'
        isAcceptable = False
      else:
        self.max_oil_press.foreground = 'black'
      if (self.oil_temp.text > 116 or self.oil_temp.text < 0):
        self.oil_temp.foreground = 'red'
        isAcceptable = False
      else:
        self.oil_temp.foreground = 'black'

      #750 RPM Check list
      if (self.min_oil_press.text < 10 or self.min_oil_press.text > 60):
        self.min_oil_press.foreground = 'red'
        isAcceptable = False
      else:
        self.min_oil_press.foreground = 'black'
      if (self.cht_min.text > 238 or self.cht_min.text < 0):
        self.cht_min.foreground = 'red'
        isAcceptable = False
      else:
        self.cht_min.foreground = 'black'
      if (self.mixture_dilute.text > 50 or self.mixture_dilute.text < 25):
        self.mixture_dilute.foreground = 'red'
        isAcceptable = False
      else:
        self.mixture_dilute.foreground = 'black'

      #Fuel Flow Pressure Check list
      if (self.unmetered_ffp_min.text < 8 or self.unmetered_ffp_min.text > 10 ):
        self.unmetered_ffp_min.foreground = 'red'
        isAcceptable = False
      else:
        self.unmetered_ffp_min.foreground = 'black'
      if (self.max_rpm.text > 2700 or self.max_rpm.text < 2650):
        self.max_rpm.foreground = 'red'
        isAcceptable = False
      else:
        self.max_rpm.foreground = 'black'
      if (self.max_rpm.text >= 2690 and self.max_rpm.text <=2700):
        if (self.metered_ffp_max.text > 18.4 or self.metered_ffp_max.text < 16.5):
          self.metered_ffp_max.foreground = 'red'
          isAcceptable = False
        else:
          self.metered_ffp_max.foreground = 'black'
      if (self.max_rpm.text >= 2670 and self.max_rpm < 2690):
        if (self.metered_ffp_max.text > 18.2344 or self.metered_ffp_max.text < 16.3515):
          self.metered_ffp_max.foreground = 'red'
          isAcceptable = False
        else:
          self.metered_ffp_max.foreground = 'black'
      if (self.max_rpm.text >= 2650 and self.max_rpm < 2670):
        if (self.metered_ffp_max.text > 18.0688 or self.metered_ffp_max.text < 16.203):
          self.metered_ffp_max.foreground = 'red'
          isAcceptable = False
        else:
          self.metered_ffp_max.foreground = 'black'
      if (self.unmetered_ffp_max.text > 36.2 or self.unmetered_ffp_max.text < 29.2):
        self.unmetered_ffp_max.foreground = 'red'
        isAcceptable = False
      else:
        self.unmetered_ffp_max.foreground = 'black'
      if (self.metered_ffp_min.text > 4.5 or self.metered_ffp_min.text < 3.9):
        self.metered_ffp_min.foreground = 'red'
        isAcceptable = False
      else:
        self.metered_ffp_min.foreground = 'black'

    if (isAcceptable):
      Notification("הבדיקה שמישה, כל הנתונים במגבלות",
             title="!שמיש",
             style="success").show()
      all_the_data = [self.right_magneto, self.left_magneto, 
                   self.manifold_press,
                   self.max_ff, self.cht_max, self.max_oil_press,
                   self.oil_temp,
                   self.metered_ffp_min, self.unmetered_ffp_min, 
                   self.metered_ffp_max,
                   self.unmetered_ffp_max, self.max_rpm]
      for field in all_the_data:
        field.foreground = 'black'
      
    else:
      Notification("יש נתונים אשר לא עומדים במגבלות הספרות",
             title="!לא שמיש",
             style="danger").show()
        
      
      
      
      
