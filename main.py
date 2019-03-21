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


if len(sys.argv) == 1:
    # create cities
    for i in range(0, 15):
        cityList.append(salesman_objects.City(x=int(random.random() * 200),
                                            y=int(random.random() * 200)))

    # pprint(cityList)
    # get best route between them
    gen = salesman_genetics.GeneticAlgorithm(cityList, 120, 30, 0.01, original_crossover_method=True, original_mutation_method=True)
    gen2 = salesman_genetics.GeneticAlgorithm(cityList, 120, 30, 0.01, original_crossover_method=False, original_mutation_method=True)
    gen3 = salesman_genetics.GeneticAlgorithm(cityList, 120, 30, 0.01, original_crossover_method=True, original_mutation_method=False)
    gen.run(200)
    gen2.run(200)
    gen3.run(200)

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

    print("Original crossover and mutation")
    salesman_graphics.Plot_gen(gen.gen_bests)
    print("Original crossover and mutation done")
    print("Modified crossover next")
    salesman_graphics.Plot_gen(gen2.gen_bests)
    print("Modified crossover done")
    print("Modified mutation next")
    salesman_graphics.Plot_gen(gen3.gen_bests)
    print("Modified mutation done")

    print("Cost for original crossover and mutation (distance):", 1/gen.gen_bests[len(gen.gen_bests)-1][1])
    print("Cost for modified crossover (distance):", 1/gen2.gen_bests[len(gen2.gen_bests)-1][1])
    print("Cost for modified mutation (distance):", 1/gen3.gen_bests[len(gen3.gen_bests)-1][1])

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
            nums = re.split(r"\s?[, ]\s?", line)
            cityList.append(salesman_objects.City(
                x=int(nums[0]), y=int(nums[1])))
        gen = salesman_genetics.GeneticAlgorithm(
            cityList, pop_size, mating_pool_size, mutation_rate, original_crossover_method=True, original_mutation_method=True)
        gen.run(generations)

        pprint(gen.gen_bests[len(gen.gen_bests)-1])
        print("Cost (distance):", 1/gen.gen_bests[len(gen.gen_bests)-1][1])

        salesman_graphics.Plot_gen(gen.gen_bests)
    else:
        f = open(filename, "r")
        lines = f.readlines()
        i = 0
        for line in lines:
            nums = re.split(r"\s?[, ]\s?", line)
            cityList.append(salesman_objects.distCity(i, nums))
            i += 1
        gen = salesman_genetics.GeneticAlgorithm(
            cityList, pop_size, mating_pool_size, mutation_rate, original_crossover_method=True, original_mutation_method=True)
        gen.run(generations)

        pprint(gen.gen_bests[len(gen.gen_bests) - 1])
        print("Cost (distance):", 1/gen.gen_bests[len(gen.gen_bests)-1][1])

else:
    print("Usage: python(3) main.py \"filename\" population_size mating_pool_size mutation_rate number_generations xy_city_loc")
    print("for xy_city_loc enter 0 for distance matrix and 1 for x,y locations")
