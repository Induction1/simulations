import numpy as np
import matplotlib.pyplot as plt

from dovehawk.survivability_methods import instantiate_population, run_simulation


def histogram_view(pop_count, num_cycles, food):
    cycles = num_cycles
    population = instantiate_population(pop_count)

    array_population = run_simulation(population, cycles, food)

    labels = np.arange(cycles + 1)
    dove = array_population[1]
    hawks = array_population[2]
    width = 0.35

    fig, ax = plt.subplots()

    ax.bar(labels, dove, width, bottom=None, label='Doves')
    ax.bar(labels, hawks, width, bottom=dove,
           label='Hawks')

    ax.set_ylabel('amount')
    ax.set_title('Test')
    ax.legend()

    plt.show()


def stacked_area(pop_count, num_cycles, food):
    cycles = num_cycles
    population = instantiate_population(pop_count)

    array_population = run_simulation(population, cycles, food)
    labels = np.arange(cycles + 1)

    plt.stackplot(labels, array_population[1], array_population[2], labels=['Dove', 'Hawk'])
    plt.legend(loc='upper left')

    plt.show()
