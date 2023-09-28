import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.mpl_util

import numpy as np
import matplotlib.pyplot as plt

@anvil.server.callable
def cost_plot(cost):
  x = [1]
  y = [cost]
  
  # Plot it in the normal Matplotlib way
  plt.scatter(x,y, color= "crimson", marker='o')
  
  # Return this plot as a PNG image in a Media object, MPL means matplotlib
  return anvil.mpl_util.plot_image()
@anvil.server.callable
  

def make_plot1():
  # Create random 
  x = np.linspace(0.0, 15.0, 5)
  y = np.random.rand(5)
  
  # Plot it in the normal Matplotlib way
  plt.figure(1, figsize=(10,5))
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

  




