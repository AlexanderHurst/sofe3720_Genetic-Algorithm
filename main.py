# The traveling salesman problem
# Using a genetic algorithm to solve it

# References: Evolution of a salesman: A complete genetic algorithm tutorial for Python (Eric Stoltz, 2018)

import random
from pprint import pprint

import time

import salesman_objects
import salesman_genetics
import salesman_graphics

cityList = []

# create cities
for i in range(0, 60):
    cityList.append(salesman_objects.City(x=int(random.random() * 200),
                                          y=int(random.random() * 200)))

# pprint(cityList)
# get best route between them
gen = salesman_genetics.GeneticAlgorithm(cityList, 100, 20, 0.01)
gen.run(900)

salesman_graphics.Plot_gen(gen.gen_bests)

# pprint(gen.pop)