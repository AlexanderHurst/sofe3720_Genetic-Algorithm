# Classes used in main.py and functions.py

import numpy as np
import random
import operator

# CLASS: City
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = np.sqrt((x_distance ** 2) + (y_distance ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# CLASS: Fitness
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    # get the route distance for a section
    def route_Distance(self):
        # check if the distance is 0
        if self.distance == 0:
            #if yes: create a path_distnace
            path_distance = 0

            # for the entire length of the route
            for i in range(0, len(self.route)):
                from_city = self.route[i]
                to_city = None

                if i + 1 < len(self.route):
                    to_city = self.route[i+1]
                else:
                    to_city = self.route[0]
                
                path_distance += from_city.distance(to_city)
            
            self.distance = path_distance

        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_Distance())
        return self.fitness