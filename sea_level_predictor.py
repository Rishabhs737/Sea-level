import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize = (15,10))
    plt.scatter(x = 'Year', 
                y = 'CSIRO Adjusted Sea Level',
                data = df)
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_years = np.arange(df['Year'].min(), 2051)
    y = res.slope * extended_years + res.intercept
    plt.plot(extended_years, y, color='red', label='Best Fit Line 1880-2050')
    
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    after_two_thousands = np.arange(2000, 2051)
    y_after_two_thousands = res_2000.slope * after_two_thousands + res_2000.intercept
    plt.plot(after_two_thousands, y_after_two_thousands, color='green', label='Best Fit Line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()