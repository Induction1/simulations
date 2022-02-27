import math
import random
from typing import List

from dovehawk.subject import Subject


def instantiate_population(n=1) -> List[Subject]:
    """Instantiates a population of n subjects"""
    population = [Subject(random.randint(0, 1)) for _ in range(n)]
    return population


def interact(a, b):
    if a is None and b is None:
        pass
    else:
        if a is None:
            b.energy += 1
        elif b is None:
            a.energy += 1
        else:
            if a.type == 0 and b.type == 0:
                a.energy += 0.5
                b.energy += 0.5
            elif a.type == 1 and b.type == 1:
                a.energy -= 0.5
                b.energy -= 0.5
            elif a.type == 0 and b.type == 1:
                b.energy += 1
            else:
                a.energy += 1


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
    return population
