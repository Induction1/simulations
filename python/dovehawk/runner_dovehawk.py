from dovehawk.subject import Subject
from dovehawk.survivability_methods import instantiate_population, food_hunt, interact

population = instantiate_population(3)

food_hunt(population, 5)