import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.mpl_util

import numpy as np
import matplotlib.pyplot as plt

@anvil.server.callable
def cost_plot(testrun,runcost):
  x = [testrun]
  y = [runcost]
  
  # Plot it in the normal Matplotlib way
  plt.figure(figsize=(10,6))
  plt.scatter(x,y, color= "crimson", marker='o')
  plt.xlabel('Test Run', fontsize=14)  # You can adjust the font size (e.g., 14)
  plt.ylabel('Cost Catalyst', fontsize=14)
  # Return this plot as a PNG image in a Media object, MPL means matplotlib
  return anvil.mpl_util.plot_image()
@anvil.server.callable
  

def make_plot1():
  # Create random 
  x = np.linspace(0.0, 15.0, 5)
  y = np.random.rand(5)
  
  # Plot it in the normal Matplotlib way
 
  plt.figure(1, figsize=(10,10))
  plt.plot(x, y, 'crimson')  
  
  # Return this plot as a PNG image in a Media object, MPL means matplotlib
  return anvil.mpl_util.plot_image()

@anvil.server.callable
def make_plot2():
  # Create random 
  x = np.linspace(0.0, 7.0, 5)
  y = np.random.rand(5)
  
  # Plot it in the normal Matplotlib way
  plt.figure(1, figsize=(10,5))
  plt.plot(x, y, 'crimson')  
  
  # Return this plot as a PNG image in a Media object, MPL means matplotlib
  return anvil.mpl_util.plot_image()

@anvil.server.callable
def make_plot3():
  # Create random 
  x = np.linspace(0.0, 25.0, 5)
  y = np.random.rand(5)
  
  # Plot it in the normal Matplotlib way
  plt.figure(1, figsize=(10,5))
  plt.plot(x, y, 'crimson')  
  
  # Return this plot as a PNG image in a Media object, MPL means matplotlib
  return anvil.mpl_util.plot_image()

  




