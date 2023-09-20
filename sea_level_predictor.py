import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  fig, ax = plt.subplots(figsize=(7,5))
  ax = plt.scatter(x,y)


    # Create first line of best fit
  res = linregress(x, y)
  x_ax = pd.Series(i for i in range(1880,2051))
  y_ax = res.slope*x_ax + res.intercept
  plt.plot(x_ax,y_ax, 'r')


    # Create second line of best fit
  df2 = df.loc[df['Year']>=2000]
  x2 = df2['Year']
  y2 = df2['CSIRO Adjusted Sea Level']
  
  res2 = linregress(x2, y2)
  x_2 = pd.Series(i for i in range(2000,2051))
  y_2 = res2.slope*x_2 + res2.intercept
  plt.plot(x_2, y_2, 'green')
  


    # Add labels and title
  ax = plt.gca()
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()