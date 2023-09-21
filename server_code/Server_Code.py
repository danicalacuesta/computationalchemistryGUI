import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.mpl_util

import numpy as np
import matplotlib.pyplot as plt

@anvil.server.callable
def cost_plot():
    x_values = costpt()  # Replace with your calculated costpt values

    # Create the costpt graph plot
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, 3, 'blue')  # Use range(len(x_values)) as a placeholder for Y-axis

    # Customize the plot (add labels, titles, etc. as needed)
    plt.xlabel('Costpt Values')
    plt.ylabel('Y-axis Label')
    plt.title('Costpt vs. Y')

    # Return the costpt graph as a PNG image in a Media object
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

  




