import random
from typing import List

from dovehawk.subject import Subject


def instantiate_population(n=1) -> List[Subject]:
    """Instantiates a population of n subjects"""
    population = [Subject(random.randint(0, 1)) for i in range(50)]
    return population