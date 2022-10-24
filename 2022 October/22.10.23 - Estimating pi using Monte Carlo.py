# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:02:25 2022

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

@author: abelw
"""
import math
import random

def monte_carlo(radius = 50, dot_count = 1000):
    
    
    #Define radius of circle
    radius = radius
    
    #Define variable to track points within circle
    within_circle = 0
    
    #Define number of dots to plot
    dot_count = dot_count
    
    #Plotting and counting of random points
    for dot in range(dot_count):
        #Plotting
        x_coord = random.uniform(0,(radius*2))
        y_coord = random.uniform(0,(radius*2))
        
        #Distance calc
        distance_from_centre = math.dist([x_coord,y_coord],[radius,radius])
        if distance_from_centre <= radius:
            within_circle+=1
    
    #Estimate pi
    estimate = 4 * (within_circle / dot_count)
    return (estimate)
        

test = monte_carlo(radius = 100, dot_count = 50000)