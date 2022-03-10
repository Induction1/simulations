from dovehawk.subject import Subject
from dovehawk.survivability_methods import instantiate_population, food_hunt, interact, pass_night

population = instantiate_population(6)

for item in population:
    print(str(item.type) + ", ")

food_hunt(population, 2)
pass_night(population)

for item in population:
    print(item.type)
