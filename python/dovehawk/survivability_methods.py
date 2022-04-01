import math
import random
from typing import List

from python.dovehawk.subject import Subject


def instantiate_population(n=1) -> List[Subject]:
    """Instantiates a population of n subjects"""
    population = [Subject(random.randint(0, 1), 0) for _ in range(n)]
    return population


def interact(a, b):
    if a is None and b is None:
        pass
    else:
        if a is None:
            b.energy += 2
        elif b is None:
            a.energy += 2
        else:
            if a.type == 0 and b.type == 0:
                a.energy += 1
                b.energy += 1
            elif a.type == 1 and b.type == 1:
                a.energy -= 1
                b.energy -= 1
            elif a.type == 0 and b.type == 1:
                b.energy += 2
            else:
                a.energy += 2


def food_hunt(population, num_of_foods) -> List[Subject]:
    random.shuffle(population)

    food_array = list(range(0, num_of_foods * 2))
    random.shuffle(food_array)

    food_share = [[None for _ in range(2)] for _ in range(num_of_foods)]

    if len(population) <= 2 * num_of_foods:
        for i in range(len(population)):
            spot = food_array[i]
            food_share[math.floor(spot / 2)][spot % 2] = population[i]
    else:
        for i in range(num_of_foods * 2):
            spot = food_array[i]
            food_share[math.floor(spot / 2)][spot % 2] = population[i]

    for group in food_share:
        interact(group[0], group[1])

    return population


def pass_night(population):
    new_doves = 0
    new_hawks = 0

    population[:] = [subject for subject in population if subject.energy > 0]
    for item in population:
        if item.energy == 2:
            if item.type == 0:
                new_doves += 1
            else:
                new_hawks += 1
        item.energy = 0

    for _ in range(new_doves):
        population.append(Subject(0, 0))
    for _ in range(new_hawks):
        population.append(Subject(1, 0))

    return population


def population_statistics(population):
    total = 0
    counter = 0
    for subject in population:
        total += 1
        if subject.type == 0:
            counter += 1
    return [total, counter, total - counter]


def run_simulation(population, times, num_of_foods):
    return_arr = [[0] * (times + 1) for i in range(3)]
    statistics_zero = population_statistics(population)
    return_arr[0][0] = statistics_zero[0]
    return_arr[1][0] = statistics_zero[1]
    return_arr[2][0] = statistics_zero[2]
    for i in range(times):
        food_hunt(population, num_of_foods)
        pass_night(population)
        statistics_zero = population_statistics(population)
        return_arr[0][i + 1] = statistics_zero[0]
        return_arr[1][i + 1] = statistics_zero[1]
        return_arr[2][i + 1] = statistics_zero[2]

    return return_arr
