# The traveling salesman problem
# Using a genetic algorithm to solve it

# References: Evolution of a salesman: A complete genetic algorithm tutorial for Python (Eric Stoltz, 2018)

import random
import sys
from pprint import pprint

import time

import salesman_objects
import salesman_genetics
import salesman_graphics
import re

cityList = []

# create cities
if len(sys.argv) == 1:
    for i in range(0, 60):
        cityList.append(salesman_objects.City(x=int(random.random() * 200),
                                              y=int(random.random() * 200)))
    gen = salesman_genetics.GeneticAlgorithm(cityList, 100, 20, 0.01)
    gen.run(90)

    salesman_graphics.Plot_gen(gen.gen_bests)

elif len(sys.argv) == 7:
    filename = sys.argv[1]
    pop_size = int(sys.argv[2])
    mating_pool_size = int(sys.argv[3])
    mutation_rate = float(sys.argv[4])
    generations = int(sys.argv[5])
    xy_city_loc = int(sys.argv[6])

    if(xy_city_loc):
        f = open(filename, "r")
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            nums = re.split("\s?[, ]\s?", line)
            cityList.append(salesman_objects.City(
                x=int(nums[0]), y=int(nums[1])))
        gen = salesman_genetics.GeneticAlgorithm(
            cityList, pop_size, mating_pool_size, mutation_rate)
        gen.run(generations)

        salesman_graphics.Plot_gen(gen.gen_bests)
    else:
        f = open(filename, "r")
        lines = f.readlines()
        i = 0
        for line in lines:
            nums = re.split("\s?[, ]\s?", line)
            cityList.append(salesman_objects.distCity(i, nums))
            i += 1
        gen = salesman_genetics.GeneticAlgorithm(
            cityList, pop_size, mating_pool_size, mutation_rate)
        gen.run(generations)

        pprint(gen.gen_bests[len(gen.gen_bests) - 1])

else:
    print("Usage: python(3) main.py \"filename\" population_size mating_pool_size mutation_rate number_generations xy_city_loc")
    print("for xy_city_loc enter 0 for distance matrix and 1 for x,y locations")
