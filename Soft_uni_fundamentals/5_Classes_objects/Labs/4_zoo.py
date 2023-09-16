class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        lst = []
        t = "s"
        if species == "mammal":
            lst = self.mammals
        elif species == "fish":
            lst = self.fishes
            t = "es"
        elif species == "bird":
            lst = self.birds
        return f"{species.capitalize()}{t} in {self.zoo_name}: {', '.join(lst)}\nTotal animals: {Zoo.__animals}"


my_zoo = Zoo(input())
n = int(input())
for i in range(n):
    species, animal = input().split()
    my_zoo.add_animal(species, animal)

print(my_zoo.get_info(input()))
