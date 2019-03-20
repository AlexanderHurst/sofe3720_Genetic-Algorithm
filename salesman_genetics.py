import random
from salesman_objects import Route
from pprint import pprint
# TODO:
# implement functions

# /=========== Genetic Algorithm ===========/
class GeneticAlgorithm:
    # best_size = the number of offspring to keep when doing a crossover
    
    # The genetic algorithm is run multiple times to find the best path with variously mutated populations
    def __init__(self, city_list, pop_size, best_size, mutation_rate, original_crossover_method=True, original_mutation_method=True):
        self.pop_size = pop_size                # Initialize population size
        self.best_size = best_size              # Initialize the best size for calculations
        self.mutation_rate = mutation_rate      # Initialize the mutation rate for the mutation stage
        self.city_list = city_list              # Get the list of cities salesman must visit
        self.crossover_method = original_crossover_method
        self.mutation_method = original_mutation_method

        self.gen_bests = []

        self.pop = None                         # Start with a population of none 
        self._initialization()                  # Start creating population with route values
        self._evaluation()                      # Sort the routes based on fitness

    # 1 - INITIALIZATION
    def _initialization(self):
        # For the entire population size, add routes
        self.pop = [Route(self.city_list, True) for i in range(self.pop_size)]
    
    # Is the fitness function: sorts pop based on route
    # 2 - EVALUATION
    def _evaluation(self):
        self.pop.sort(key = lambda x: x.fitness, reverse = True)  # Sort the population based on the fitness values

    # 3 - SELECTION, using Stochastic Universal Sampling
    def _selection(self):
        # Stochastic Universal Sampling, a fitness proportinate selection
        total_fitness = sum(route.fitness for route in self.pop)    # Get the total fitness of the population
        pointer_distance = total_fitness / self.best_size           # Set the distance between pointers

        start = random.random()*pointer_distance                    # The starting point for solution intervals
        
        # Get the pointers for each section interval
        pointers = [start + (i * pointer_distance) for i in range(self.best_size)]

        mating_pool = []

        mating_pool.append(self.pop[0])

        # Choose 1 element, route, from each pointer interval
        fit_sum = self.pop[0].fitness
        i = 0
        for point in pointers:
            while fit_sum < point:
                fit_sum += self.pop[i].fitness
                i += 1
            mating_pool.append(self.pop[i])
        return mating_pool


    # Breed the population
    # 4 - Crossover method selection
    def _crossover(self, mating_pool):
        if(self.crossover_method):
            return self._crossover1(mating_pool)
        else:
            return self._crossover2(mating_pool)

    # Breed the population
    # 4 - CROSSOVER, VERSION 1
    def _crossover1(self, mating_pool):
        num_children = self.pop_size - self.best_size - 1
        children = []

        for i in range (num_children):
            parents = random.sample(mating_pool, 2)

            child = []
            
            # Create genes for the child to emerge from
            geneA = int(random.random() * len(parents[0].route))
            geneB = int(random.random() * len(parents[1].route))

            # Where the genes mix
            start_gene = min(geneA, geneB)
            end_gene = max(geneA, geneB)

            # Add the parent genes to the child
            for i in range(start_gene, end_gene):
                child.append(parents[0].route[i])
            child.extend(item for item in parents[1].route if item not in child)

            # Set a route for the child and add to list
            children.append(Route(child))
                     
        return children

    # 4 - CROSSOVER, VERSION 2
        # breeds three parents to make children
        # parent 0 usually has the most influence
        # parent 1 usually has the least influence
        # parent 2 usually has the middle influence
        # influence depending on city order and gene start + end points
    def _crossover2(self, mating_pool):
        num_children = self.pop_size - self.best_size - 1
        children = []

        for i in range (num_children):
            parents = random.sample(mating_pool, 3)

            child = []

            # Create genes for the child to emerge from
            geneA = int(random.random() * len(parents[0].route))
            geneB = int(random.random() * len(parents[1].route))
            geneC = int(random.random() * len(parents[2].route))

            genes = sorted([geneA, geneB, geneC])

            # Add the parent genes to the child
            for i in range(genes[0], genes[1]):
                child.append(parents[0].route[i])

            for i in range(genes[1], genes[2]):
                if parents[1].route[i] not in child:
                    child.append(parents[1].route[i])

            child.extend(item for item in parents[2].route if item not in child)

            # Set a route for the child and add to list
            children.append(Route(child))
                    
        return children
    
    # Mutate the population
    # 5 Mutation selection

    def _mutation(self, children):
        if(self.mutation_method):
            return self._mutation1(children)
        else:
            return self._mutation2(children)


    # Mutate the population
    # 5 - MUTATE, to defy local convergence
    def _mutation1(self, children): 
        mutants = []

        for child in children:
            for i in range(len(self.city_list)):
                if (random.random() < self.mutation_rate):
                    a = random.random()
                    child.route[int(a * len(self.city_list))], child.route[int(i)] = child.route[int(i)], child.route[int(a * len(self.city_list))]
            mutants.append(child)
        return mutants

    # Mutate the population
    # allows multiple mutations to take place per city per child
    # this shouldnt change much but does allow the possibility for more mutations
    # 5 - MUTATE, to defy local convergence
    def _mutation2(self, children): 
        mutants = []

        for child in children:
            for i in range(len(self.city_list)):
                while (random.random() < self.mutation_rate):
                    a = random.random()
                    child.route[int(a * len(self.city_list))], child.route[int(i)] = child.route[int(i)], child.route[int(a * len(self.city_list))]
            mutants.append(child)
        return mutants

    # 6 - REPEAT
    def run(self, number_of_iterations):        # Run the algorithm numerous times to get best results from mutated population
        for i in range(number_of_iterations):
            self.gen_bests.append([self.pop[0].route, self.pop[0].fitness])
            parents = self._selection()         # set the parent population     
            children = self._crossover(parents) # Breed the population
            # print("creating mutants")
            mutants = self._mutation(children)  # Mutate the population
            self.pop = parents
            self.pop.extend(mutants)            # Set the population to the mutated population
            self._evaluation()                  # Evaluate fitness
            # print("fitness:", self.pop[0].fitness)

    # Termination condition: 
    #   The termination condition has been decided to be a set number of iterations
    #   to limit the number of iterations
