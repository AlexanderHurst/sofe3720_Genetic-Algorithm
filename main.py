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


# /================================== MAIN ==================================/
# # mutate an inidividual (used by mutate population def)
# so that you dont create local convergance
# def mutate(indvidual, mutation_rate):
#     for swapped in range(len(indvidual)):
#         if (random.random() < mutation_rate):
#             swapWith = int(random.random() * len(indvidual))

#             city1 = indvidual[swapped]
#             city2 = indvidual[swapWith]

#             indvidual[swapped] = city2
#             indvidual[swapWith] = city1

#     return indvidual

# # mutate the population (calls mutate)
# def mutate_population(population, mutation_rate):
#     mutated_population = []

#     for index in range(0, len(population)):
#         mutated_index = mutate(population[index], mutation_rate)
#         mutate_population.append(mutated_index)

#     return mutate_population

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
