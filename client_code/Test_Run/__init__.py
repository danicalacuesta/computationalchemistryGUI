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
      
        #initialize for costpt graph
        self.TRc_button_click_count=0
        self.runcost= []
        #secondary element data
        #searches for button: https://chat.openai.com/c/9eac150b-167f-4c29-99e2-6b7c9de6b753
       
        self.button.data= {
          'Ti_button': {
            'EN_p': 1.54,
            'Nelec_p': 4,
            'Ed_p': 0.7,
            'Oxo_p': 1.0,
            'WF_p': 3.95,
            'Cost_p': 11.1,
            'MW_p': 47.867
          },
          'V_button': {
            'EN_p': 1.63,
            'Nelec_p': 5,
            'Ed_p': 0.4,
            'Oxo_p': 0.8,
            'WF_p': 4.10,
            'Cost_p': 357,
            'MW_p': 50.9415
          },
          'Cr_button': {
            'EN_p': 1.66,
            'Nelec_p': 6,
            'Ed_p': -0.3,
            'Oxo_p': 0.6,
            'WF_p': 4.60,
            'Cost_p': 0.094,
            'MW_p': 51.9961
          },
          'Mn_button': {
            'EN_p': 1.55,
            'Nelec_p': 7,
            'Ed_p': -0.9,
            'Oxo_p': 0.4,
            'WF_p': 3.8,
            'Cost_p': 0.0182,
            'MW_p': 54.938044
        },
        "Fe_button":  {
            'EN_p': 1.83,
            'Nelec_p': 8,
            'Ed_p': -0.8,
            'Oxo_p': 0.4,
            'WF_p': 4.30,
            'Cost_p': 0.0000424,
            'MW_p': 55.845
        },
        "Co_button": {
            'EN_p': 1.88,
            'Nelec_p': 9,
            'Ed_p': -1.5,
            'Oxo_p': 0.4,
            'WF_p': 4.40,
            'Cost_p': 0.0328,
            'MW_p': 58.933195
        },
        "NI_button": {
            'EN_p': 1.91,
            'Nelec_p': 10,
            'Ed_p': -1.6,
            'Oxo_p': 0.2,
            'WF_p': 4.50,
            'Cost_p': 0.0139,
            'MW_p': 58.6934
        },
        "Cu_button": {
            'EN_p': 1.90,
            'Nelec_p': 11,
            'Ed_p': -2.5,
            'Oxo_p': 0.2,
            'WF_p': 4.40,
            'Cost_p': 0.006,
            'MW_p': 63.546
        },
        "Zr_button" : {
            'EN_p': 1.33,
            'Nelec_p': 4,
            'Ed_p': 0.7,
            'Oxo_p': 0.8,
            'WF_p': 3.90,
            'Cost_p': 0.0357,
            'MW_p': 91.224
        },
        "Nb_button" : {
            'EN_p' : 1.60,
			      'Nelec_p' : 5,
      			'Ed_p' : 0.1,
      			'Oxo_p' : 0.8,
      			'WF_p' : 4.00,
      			'Cost_p' : 0.0614,
      			'MW_p' : 92.90638,
        },
        "Mo_button" : {
            "EN_p" : 2.16,
      			"Nelec_p" : 6,
      			"Ed_p" : -0.9,
      			"Oxo_p" : 0.6,
      			"WF_p" : 4.30,
      			"Cost_p" : 0.0401,
      			"MW_p" : 95.94,
        },
        "Tc_button" :{
            "EN_p" : 1.90,
      			"Nelec_p" : 7,
      			"Ed_p" : -1.6,
      			"Oxo_p" : 0.5,
      			"WF_p" : 4.4,
      			"Cost_p" : 100,
      			"MW_p" : 98
        },
        "Ru_button":{
            "EN_p" : 2.20,
      			"Nelec_p" : 8,
      			"Ed_p" : -1.9,
      			"Oxo_p" : 0.4,
      			"WF_p" : 4.60,
      			"Cost_p" : 10.40,
      			"MW_p" : 101.07
        },
        "Rh_button" :{
            "EN_p" : 2.28,
      			"Nelec_p" : 9,
      			"Ed_p" : -2.1,
      			"Oxo_p" : 0.3,
      			"WF_p" : 4.75,
      			"Cost_p" : 147,
      			"MW_p" : 102.9055
        },
        "Pd_button" : {
            "EN_p" : 2.20,
      			"Nelec_p" : 10,
      			"Ed_p" : -1.8,
      			"Oxo_p" : 0.0,
      			"WF_p" : 4.80,
      			"Cost_p" : 49.5,
      			"MW_p" : 106.42
        },
        "Ag_button" : {
            "EN_p" : 1.93,
      			"Nelec_p" : 11,
      			"Ed_p" : -4.0,
      			"Oxo_p" : 0.2,
      			"WF_p" : 4.30,
      			"Cost_p" : 0.521,
      			"MW_p" : 107.8682
        },
        "Hf_button" : {
            "EN_p": 1.30,
      			"Nelec_p" : 4,
      			"Ed_p" : 0.7,
      			"Oxo_p" : 1.0,
      			"WF_p" : 3.50,
      			"Cost_p" : 0.9,
      			"MW_p" : 178.49
        },
        "Ta_button": {
            "EN_p" : 1.50,
      			"Nelec_p" : 5,
      			"Ed_p" : 0.3,
      			"Oxo_p" : 0.8,
      			"WF_p" : 4.10,
      			"Cost_p" : 0.298,
      			"MW_p" : 171.9449
        },
        "W_button" : {
            "EN_p" : 2.36,
      			"Nelec_p" : 6,
      			"Ed_p" : -0.8,
      			"Oxo_p" : 0.8,
      			"WF_p" : 4.50,
      			"Cost_p" : 0.0353,
      			"MW_p" : 183.84
        },
        "Re_button":  {
            "EN_p" : 1.90,
      			"Nelec_p" : 7,
      			"Ed_p" : -1.6,
      			"Oxo_p" : 0.5,
      			"WF_p" : 5.00,
      			"Cost_p" : 3.010,
      			"MW_p" : 186.207
        },
        "Os_button" : {
            "EN_p" : 2.20,
      			'Nelec_p' : 8,
      			'Ed_p' : -2.2,
      			'Oxo_p' : 0.4,
      			'WF_p' : 4.70,
      			'Cost_p' : 12,
      			'MW_p' : 190.2
        },
        "Ir_button":  {
            'EN_p' : 2.20,
      			'Nelec_p' : 9,
      			'Ed_p' : -2.9,
      			'Oxo_p' : 0.4,
      			'WF_p' : 5.30,
      			'Cost_p' : 55.5,
      			'MW_p' : 192.22
        },
        "PT_button" : {
            'EN_p' : 2.28,
      			'Nelec_p' : 10,
      			'Ed_p' : -2.4,
      			'Oxo_p' : 0.1,
      			'WF_p ': 5.30,
      			'Cost_p' :27.8,
      			'MW_p' : 195.084
        },
        "Au_button" : {
            "EN_p ": 2.54,
      			"Nelec_p" : 11,
      			"Ed_p" : -3.4,
      			"Oxo_p" : 0.0,
      			"WF_p" : 4.30,
      			"Cost_p" : 44.8,
      			"MW_p" : 196.96657
        }
        }  

        # Initialize button click flags to False
        self.selected_button= None
        self.MW_mpt = 195.084
        self.mol_p = 100
        self.percent = 0  # Initialize percent to 0

    def set_button_attributes(self, button):
      button_data = button.data
      self.EN_p = button_data['EN_p']
      self.Nelec_p = button_data['Nelec_p']
      self.Ed_p = button_data['Ed_p']
      self.Oxo_p = button_data['Oxo_p']
      self.WF_p = button_data['WF_p']
      self.Cost_p = button_data['Cost_p']
      self.MW_p = button_data['MW_p']
      self.selected_button = button

    def TI_button_clicked(self, **event_args):
        """This method is called when this radio button is selected"""
        # Access the stored variables directly from the 'data' attribute of the 'TI' button
        self.set_button_attributes(self.TI_button)
    def V_button_clicked(self, **event_args):
        """This method is called when this radio button is selected"""
        self.set_button_attributes(self.V_button)
    # TI and V are secondary metals you can choose from
    def costpt(self, **event_args):
        """This method is called when this radio button is selected"""
        try:
            # Get the percentage value from the "SM_input" text box and convert it to a float
            self.percent = float(self.SM_input.text)/100
        except ValueError:
            # If the input cannot be converted to a float, set a default percentage value
            self.percent = 0.0001
        self.mol_m = (1 - self.percent) / self.percent * self.mol_p

        if self.selected_button is not None:
            button_name = self.selected_button.name
            button_info = self.button_data.get(button_name)
            if button_info:
                self.MW_p = button_info['MW_p']
                self.Cost_p = button_info['Cost_p']
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
        
    def TRc_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.TRc_button_click_count += 1
    
        if self.selected_button is not None:
          testrun= list(range(1, self.TRc_button_click_count + 1))
          self.costpt()
          self.runcost.append(self.Cost)  # Append the cost to the list
          media_obj = anvil.server.call('cost_plot', testrun, self.runcost)
          self.image_2.source = media_obj
          
        else:
            # Display an error message or handle the case when no button is selected
            self.CC_label.text = "Please select a metal button first."

    

