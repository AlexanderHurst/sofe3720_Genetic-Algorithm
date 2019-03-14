# The traveling salesman problem
# Using a genetic algorithm to solve it

# TASKS
#   1. Seperate into 3 files: Classes, Functions, Main Program


# References: Evolution of a salesman: A complete genetic algorithm tutorial for Python (Eric Stoltz, 2018)

import numpy as np
import math
import random
import operator
import pandas as pd 
from matplotlib import pyplot as plt

cityList = []

# /================================== CLASSES ==================================/
# CLASS: City
class City:
    # initiate the city
    def __init__(self, x, y):
        self.x = None
        self.y = None

        # Assign values to City
        if x is not None:
            self.x = x
        else:
            self.x = random.randint * 200

        if y is not None:
            self.y = y
        else:
            self.y = random.randint * 200
        
    # get coordinates X
    def get_x(self):
        return self.x
    
    # get coordinates Y
    def get_y(self):
        return self.y
    
    # get euclid distance between 2 cities
    def distance(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = np.sqrt((x_distance ** 2) + (y_distance ** 2))
        return distance

    # self representation
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# CLASS: Salesman <-- dont think i need or use this..
class Salesman:
    destination_cities = []

    # to trip add a city
    def add_city(self, city):
        self.destination_cities.append(city)

    # return the route
    def get_salesman_route(self, index):
        return self.destination_cities[index]

    # get the number of cities on route
    def get_number_of_cities(self):
        return len(self.destination_cities)    


# CLASS: Fitness
class Fitness:
    # initiate the route
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

    # get fitness function for route
    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_Distance())
        return self.fitness

# /================================== FUNCTIONS ==================================/
# create a route from one cities to citites
def create_Route(city_list):
    route = random.sample(city_list, len(city_list))
    return route

# get and initiate initial population
def initial_population(pop_size, city_list):
    population = []

    for i in range(0, pop_size):
        population.append(create_Route(city_list))

    return population

# rank the routes on their population
def rank_routes(population):
    best_route_results = {}
    for i in range(0, len(population)):
        best_route_results[i] = Fitness(population[i]).route_fitness()
    return sorted(best_route_results.items(), key = operator.itemgetter(1), reverse = True)

# select routes given their fitness
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

# create a mating pool
def mating_pool(population, selection_results):
    mating_pool = []

    for i in range(o, len(selection_results)):
        index = selection_results[i]
        mating_pool.append(population[index])

    return mating_pool

# breed two parents and generate a child
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

# breed the population
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

# mutate an inidividual (used by mutate population def)
def mutate(indvidual, mutation_rate):
    for swapped in range(len(indvidual)):
        if (random.random() < mutation_rate):
            swapWith = int(random.random() * len(indvidual))

            city1 = indvidual[swapped]
            city2 = indvidual[swapWith]

            indvidual[swapped] = city2
            indvidual[swapWith] = city1
    
    return indvidual

# mutate the population (calls mutate)
def mutate_population(population, mutation_rate):
    mutated_population = []

    for index in range(0, len(population)):
        mutated_index = mutate(population[index], mutation_rate)
        mutate_population.append(mutated_index)

    return mutate_population

# get the values of the next generation of population
def next_gen(current_generation, best_size, mutation_rate):
    popRanked = rank_routes(current_generation)
    selectionResults = selection(pop_ranked, best_size)
    matingPool = mating_pool(current_generation, selectionResults)
    children = breed_population(matingPool, best_size)
    next_gen = mutate_population(children, mutation_rate)
    return next_gen

# this is the genetic algorithm: gets best route for travel
def geneticAlgorithm(population, pop_size, best_size, mutation_rate, generations):
    pop = initial_population(pop_size, population)

    print( "Initial Distance: " + str( 1 / rank_routes(pop)[0][1] ) )

    for i in range(0, generations):
        pop = next_gen(pop, best_size, mutation_rate)

    print( "Final Distance: " + str( 1 / rank_routes(pop)[0][1] ) ) 
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]

    return best_route

# plot the best route (matplotlib)
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


# /================================== MAIN ==================================/

# create cities
for i in range(0, 25):
    cityList.append(City(x = int(random.random() * 200), y = int(random.random()) * 200) )

# get best route between them
geneticAlgorithm(cityList, 100, 20, 0.01, 500)
geneticAlgorithmPlot(population = cityList, pop_size = 100, best_size = 20, mutation_rate = 0.01, generations = 500)

