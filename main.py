# # The traveling salesman problem
# # Using a genetic algorithm to solve it

# # TASKS
# #   1. 


# # References: Evolution of a salesman: A complete genetic algorithm tutorial for Python (Eric Stoltz, 2018)

# import numpy as np
# import math
import random
from pprint import pprint
# import operator
# import pandas as pd

import salesman_objects
import salesman_genetics
cityList = []

# create cities
for i in range(0, 15):
    cityList.append(salesman_objects.City(x=int(random.random() * 200),
                                          y=int(random.random() * 200)))

pprint(cityList)
# get best route between them
gen = salesman_genetics.GeneticAlgorithm(cityList, 50, 10, 0.02)
gen.run(25)
pprint(gen.pop)

# geneticAlgorithmPlot(population = cityList, pop_size = 100, best_size = 20, mutation_rate = 0.01, generations = 500)
