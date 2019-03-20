import random
import numpy as np

# /=========== CLASS: City ===========/


class distCity:
    # Initiate the city
    def __init__(self, city_num, city_dists=[]):
        self.city_num = city_num
        self.city_dists = city_dists

    # get distance between 2 cities
    def distance(self, city):
        return float(self.city_dists[city.city_num])

    # self representation of a city
    def __repr__(self):
        return "City: " + str(self.city_num)


class City:
    # Initiate the city
    def __init__(self, x=None, y=None):
        self.x = None
        self.y = None

        # Assign values to City, randomly generate if no values are given
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

    # self representation of a city
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


# /=========== CLASS: Route ===========/
class Route:
    def __init__(self, city_list, randomize=False):
        if(randomize):
            self.randomize_start(city_list)
        else:
            self.route = city_list
        self.fitness = None
        self.calc_fitness()

    def randomize_start(self, city_list):
        self.route = random.sample(city_list, len(city_list))

    # Note: the best fitness is the shortest route between all cities on the path
    def calc_fitness(self):
        self.fitness = 1/sum(self._calc_dist_to_next(i)
                             for i in range(len(self.route)))

    def _calc_dist_to_next(self, index):
        return self.route[index % len(self.route)].distance(self.route[(index+1) % len(self.route)])

    def __repr__(self):
        return "Fitness: " + str("{0:.3E}".format(self.fitness)) + "\tRoute: " + str(self.route)
