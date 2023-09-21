from ._anvil_designer import Test_RunTemplate
from anvil import *
from ..Results import Results
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.tables import app_tables



class Test_Run(Test_RunTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run when the form opens.
        # Store the variables in the 'TI' button's data attribute
        self.TI_button.data = {
            'EN_p': 1.54,
            'Nelec_p': 4,
            'Ed_p': 0.7,
            'Oxo_p': 1.0,
            'WF_p': 3.95,
            'Cost_p': 11.1,
            'MW_p': 47.867
        }
        self.V_button.data = {
            'EN_p': 1.63,
            'Nelec_p': 5,
            'Ed_p': 0.4,
            'Oxo_p': 0.8,
            'WF_p': 4.10,
            'Cost_p': 357,
            'MW_p': 50.9415
        }
        # Initialize button click flags to False
        self.selected_button= None
        self.MW_mpt = 195.084
        self.mol_p = 100
        self.percent = 0  # Initialize percent to 0
        
    # TI and V are secondary metals you can choose from
    def costpt(self, **event_args):
        """This method is called when this radio button is selected"""
        try:
            # Get the percentage value from the "SM_input" text box and convert it to a float
            self.percent = float(self.SM_input.text)
        except ValueError:
            # If the input cannot be converted to a float, set a default percentage value
            self.percent = 0.0001
        self.mol_m = (1 - self.percent) / self.percent * self.mol_p

        if self.TI_button_clicked:
            self.MW_p = self.TI_button.data['MW_p']
            self.Cost_p = self.TI_button.data['Cost_p']
        elif self.V_button_clicked:
            self.MW_p = self.V_button.data['MW_p']
            self.Cost_p = self.V_button.data['Cost_p']
        else:
            # Set a default value if neither TI_button nor V_button is clicked
            self.MW_p = 0
            self.Cost_p = 0
        
        self.kg_p = self.mol_p * self.MW_p / 1000
        self.kg_m = self.mol_m * self.MW_mpt / 1000
        self.Cost = (self.kg_p * self.Cost_p + self.kg_m * 27800) / (self.kg_p + self.kg_m) / 1000
        self.CC_label.text = f"Cost of Catalyst: {self.Cost:.2f} $/kg"

    def Pt_button_clicked(self, **event_args):
      """This method is called when this radio button is selected"""
      self.selected_button = self.Pt_button
      self.costpt()
      
    def TI_button_clicked(self, **event_args):
        """This method is called when this radio button is selected"""
        # Access the stored variables directly from the 'data' attribute of the 'TI' button
        TI_data = self.TI_button.data
        self.EN_p = TI_data['EN_p']
        self.Nelec_p = TI_data['Nelec_p']
        self.Ed_p = TI_data['Ed_p']
        self.Oxo_p = TI_data['Oxo_p']
        self.WF_p = TI_data['WF_p']
        self.Cost_p = TI_data['Cost_p']
        self.MW_p = TI_data['MW_p']
        self.selected_button = self.TI_button
        self.costpt()

    def V_button_clicked(self, **event_args):
        """This method is called when this radio button is selected"""
        V_data = self.V_button.data
        self.EN_p = V_data['EN_p']
        self.Nelec_p = V_data['Nelec_p']
        self.Ed_p = V_data['Ed_p']
        self.Oxo_p = V_data['Oxo_p']
        self.WF_p = V_data['WF_p']
        self.Cost_p = V_data['Cost_p']
        self.MW_p = V_data['MW_p']
        self.selected_button = self.V_button
        self.costpt()
    #Graphing functions
    
        
    def TRc_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        
        #cost_obj = anvil.server.call('cost_plot')
        #media_obj1 = anvil.server.call('make_plot1')
        #media_obj2 = anvil.server.call('make_plot2')
        #media_obj3 = anvil.server.call('make_plot3')
        #self.image_1.source = cost_obj
        #self.image_2.source = media_obj1
        #self.image_3.source = media_obj2
        #self.image_4.source = media_obj3
        if self.selected_button is not None:
          self.costpt()
        else:
            # Display an error message or handle the case when no button is selected
            self.CC_label.text = "Please select a metal button first."

    

