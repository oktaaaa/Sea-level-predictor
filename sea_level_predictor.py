import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    x= df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)  

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_1 = np.arange(df['Year'].min(),2051)
    y_1 = slope*x_1 + intercept

    plt.plot(x_1,y_1, color = 'orange')

    # Create second line of best fit
    year_2000 = df[df['Year'] >= 2000]
    

    slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = linregress(year_2000['Year'],year_2000['CSIRO Adjusted Sea Level'])

    x_2 = np.arange(2000,2051)
    y_2 = slope_2* x_2 + intercept_2

    plt.plot(x_2,y_2, color = 'blue')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
