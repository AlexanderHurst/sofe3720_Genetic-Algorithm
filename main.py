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
for i in range(0, 15):
    cityList.append(salesman_objects.City(x=int(random.random() * 200),
                                          y=int(random.random() * 200)))

# pprint(cityList)
# get best route between them
gen = salesman_genetics.GeneticAlgorithm(cityList, 120, 30, 0.01, original_crossover_method=True, original_mutation_method=True)
gen2 = salesman_genetics.GeneticAlgorithm(cityList, 120, 30, 0.01, original_crossover_method=False, original_mutation_method=True)
gen3 = salesman_genetics.GeneticAlgorithm(cityList, 120, 30, 0.01, original_crossover_method=True, original_mutation_method=False)
gen.run(400)
gen2.run(400)
gen3.run(400)

for i, best_one, best_two, best_three in zip(range(len(gen.gen_bests)), gen.gen_bests, gen2.gen_bests, gen3.gen_bests):
    print("generation", i)
    print("Original crossover and mutation")
    pprint(best_one)
    print()
    print("Modified crossover")
    pprint(best_two)
    print()
    print("Modified mutation")
    pprint(best_three)
    print()

salesman_graphics.Plot_gen(gen.gen_bests)

# pprint(gen.pop)