population = list(map(int, input().split(", ")))
min_wealth = int(input())
for index, item in enumerate(population):
    if item < min_wealth:
        most_wealth = population.index(max(population))
        added = (min_wealth - population[index])
        population[most_wealth] -= added
        population[index] += added

is_distributed = True
for i in population:
    if i < min_wealth:
        is_distributed = False

if not is_distributed:
    print("No equal distribution possible")
else:
    print(population)
