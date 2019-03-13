# The traveling salesman problem
# Using a genetic algorithm to solve it

import numpy as np
import random
import operator
import pandas as pd 
from matplotlib import pyplot as plt
from functions import *

cityList = []

for i in range(0, 25):
    cityList.append(City(x = int(random.random() * 200), y = int(random.random()) * 200) )

geneticAlgorithm(cityList, 100, 20, 0.01, 500)
geneticAlgorithmPlot(population = cityList, pop_size = 100, best_size = 20, mutation_rate = 0.01, generations = 500)

