"""
title:          TPK4161_problem_2_1
version:        1.0.0
fileName:       events.py 
author:         Joachim Nilsen Grimstad

description:    Solution to TPK4161_problem_2_1
                                
license:       GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html 
                
disclaimer:     Author takes no responsibility for any use other than authors own evaluation in courses at NTNU.
    
""" 

import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def normal_distribution_function(x, mu, sigma):
    return (1 / math.sqrt(2 * math.pi)) * (1 / sigma) * (math.exp(-1 * ((x - mu)**2 / (2 * sigma**2))))

def integrate_composite_simpsons_rule(func, mu, sigma, lower_limit, upper_limit, n):
    # Composite simpson's rule
    dx = (upper_limit - lower_limit) / n
    I = func(lower_limit, mu, sigma)
    for k in range(1, n):
        if k % 2 == 0:
            I += 2 * func(lower_limit + (dx * k), mu, sigma)
        else:
            I += 4 * func(lower_limit + (dx * k), mu, sigma)
    I += func(upper_limit, mu, sigma)
    I = dx * ( I / 3)
    return I 

if __name__ == '__main__':
    # Numerical integration
    mu = 5
    sigma = 3
    lower_limit = 3
    upper_limit = 6
    n = 20
    area = integrate_composite_simpsons_rule(normal_distribution_function, mu, sigma, lower_limit, upper_limit, n)
    print(f'The probability that that X is larger than {lower_limit} and less or equal to {upper_limit} is {area}') 

    # Rest of the code is to get a nice plot for the assignment...

    data = np.random.normal(mu, sigma, 1000000) # generate 100000 points data where X ~ N(mu, sigma)  
    plot = sns.kdeplot(data, color = 'black') # Plot the PDF of the data using kernel density estimation
    data_x, data_y = plot.get_lines()[0].get_data() # Extract the x, y coordinates of the plotted PDF
    y_lower = np.interp(lower_limit, data_x, data_y) # interpolates the y values for x = lower_limit
    y_upper = np.interp(upper_limit, data_x, data_y) # interpolates the y values for x = upper_limit
    fill_x = [lower_limit]  # x-values of the filled in area under the curve
    fill_y = [y_lower] # y-values of the filled in area under the curve
    for i in range (len(data_x)): # Logic that appends the relevant data points to fill in under the curve for x = lower_limit to x = upper_limit 
        if data_x[i] > lower_limit and data_x[i] < upper_limit:
            fill_x.append(data_x[i])
            fill_y.append(data_y[i])
    fill_x.append(upper_limit)
    fill_y.append(y_upper)
    plt.ylim(bottom = 0) # sets minimum limit on y axis.
    plt.fill_between(x = fill_x, y1 = fill_y, color = 'blue') # fills in the area
    plt.show()

    # Simulation Test
    counter = 0
    for X in data:
        if X > lower_limit and X <= upper_limit:
            counter += 1
    prob = counter / len(data)
    print(prob)

