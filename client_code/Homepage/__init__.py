from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
import anvil.server
from ..Test_Run import Test_Run


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def ATR_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_test_run = Test_Run()
    ATR_clicked = alert(content=new_test_run, title="Add Test Run", large=True)
    
   

  
    
      

   