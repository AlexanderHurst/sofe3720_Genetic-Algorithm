from matplotlib import pyplot as plt


# plot the best route (matplotlib)
def geneticAlgorithmPlot(progress):
    # pop = initial_population(pop_size, population)
    # progress = []
    # progress.append(1/rank_routes(pop)[0][1])

    # for i in range(0, generations):
    #     pop = next_gen(pop, best_size, mutation_rate)
    #     progress.append(1/rank_routes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()
