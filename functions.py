# Functions used in main.py

import numpy as np
import random
import operator
import pandas as pd 
from classes import *
import matplotlib.pyplot as plt


def create_Route(city_list):
    route = random.sample(city_list, len(city_list))
    return route


def initial_population(pop_size, city_list):
    population = []

    for i in range(0, pop_size):
        population.append(create_Route(city_list))

    return population


def rank_routes(population):
    best_route_results = {}
    for i in range(0, len(population)):
        best_route_results[i] = Fitness(population[i]).route_fitness()
    return sorted(best_route_results.items(), key = operator.itemgetter(1), reverse = True)


def selection(pop_ranked, best_size):
    selection_results = []

    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_percentage'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range (0, best_size):
        selection_results.append(pop_ranked[i][0])
    for i in range(0, len(pop_ranked) - best_size):
        pick = 100 * random.random()
        for i in range(o, len(pop_ranked)):
            if pick <= df.iat[i,3]:
                selection_results.append(pop_ranked[i][0])
                break
    
    return selection_results


def mating_pool(population, selection_results):
    mating_pool = []

    for i in range(o, len(selection_results)):
        index = selection_results[i]
        mating_pool.append(population[index])

    return mating_pool


def breed(parent1, parent2):
    child = []
    child_p1 = []
    child_p2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    start_gene = min(geneA, geneB)
    end_gene = max(geneA, geneB)

    for i in range(start_gene, end_gene):
        child_p1.append(parent1[i])

    child_p2 = [item for item in parent2 if item not in child_p1]

    child = child_p1 + child_p2

    return child


def breed_population(mating_pool, best_size):
    children = []
    length = len(mating_pool) - best_size
    pool = random.sample(mating_pool, len(mating_pool))

    for i in range(0, best_size):
        children.append(mating_pool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(mating_pool)-i-1])
        children.append(child)

    return children


def mutate(indvidual, mutation_rate):
    for swapped in range(len(indvidual)):
        if (random.random() < mutation_rate):
            swapWith = int(random.random() * len(indvidual))

            city1 = indvidual[swapped]
            city2 = indvidual[swapWith]

            indvidual[swapped] = city2
            indvidual[swapWith] = city1
    
    return indvidual


def mutate_population(population, mutation_rate):
    mutated_population = []

    for index in range(0, len(population)):
        mutated_index = mutate(population[index], mutation_rate)
        mutate_population.append(mutated_index)

    return mutate_population


def next_gen(current_generation, best_size, mutation_rate):
    popRanked = rank_routes(current_generation)
    selectionResults = selection(pop_ranked, best_size)
    matingPool = mating_pool(current_generation, selectionResults)
    children = breed_population(matingPool, best_size)
    next_gen = mutate_population(children, mutation_rate)
    return next_gen


def geneticAlgorithm(population, pop_size, best_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)

    print( "Initial Distance: " + str( 1 / rank_routes(pop)[0][1] ) )

    for i in range(0, generations):
        pop = next_gen(pop, best_size, mutation_rate)

    print( "Final Distance: " + str( 1 / rank_routes(pop)[0][1] ) ) 
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]

    return best_route


def geneticAlgorithmPlot(population, pop_size, best_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)
    progress = []
    progress.append(1/rank_routes(pop)[0][1])

    for i in range(0, generations):
        pop = next_gen(pop, best_size, mutation_rate)
        progress.append(1/rank_routes(pop)[0][1])

    
    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()