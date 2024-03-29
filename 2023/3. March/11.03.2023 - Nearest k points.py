"""
Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

points = [(0, 0), (5, 4), (3, 1)]

import math

def nearest_k_points(points, centre, k):

    distance_dict = dict()

    for point in points:
        distance_dict[math.dist(point, centre)] = point
    
    distances = list(distance_dict.keys())
    distances.sort()
    
    output = list()

    for distance in distances[0:k]:
        output.append(distance_dict.get(distance))

    print(output)
        

print(nearest_k_points(points, (0,0), 2))
