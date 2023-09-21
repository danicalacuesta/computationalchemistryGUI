from ._anvil_designer import ResultsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Results(ResultsTemplate):
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    media_obj = anvil.server.call('make_plot')
    media_obj1 = anvil.server.call('make_plot1')
    media_obj2 = anvil.server.call('make_plot2')
    media_obj3 = anvil.server.call('make_plot3')
    self.image_1.source = media_obj
    self.image_2.source= media_obj1
    self.image_3.source= media_obj2
    self.image_4.source= media_obj3

   
   
 