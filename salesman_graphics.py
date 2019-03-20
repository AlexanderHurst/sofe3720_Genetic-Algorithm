from matplotlib import pyplot as plt
from matplotlib import path
from salesman_objects import City
import numpy as np
import random

# plot the best route (matplotlib)


def Plot_gen(routes):
    for route in routes:
        plt.clf()
        print(route[0])
        points = np.array([[city.get_x(), city.get_y()]
                           for city in route[0]])
        new_point = np.array([[route[0][0].get_x(), route[0][0].get_y()]])

        points = np.append(points, new_point, axis=0)

        plt.plot(*points.T)

        plt.pause(0.01)

    plt.show()
