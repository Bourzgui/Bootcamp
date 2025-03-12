class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    #add 
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to {self.name}")
        else:
            print(f"{new_animal} is already in {self.name}")
    
    def get_animals(self):
        print("\nAnimals in", self.name + ":")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.name}")
        else:
            print(f"{animal_sold} is not in {self.name}")
    
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in sorted_animals:
                if isinstance(sorted_animals[first_letter], list):
                    sorted_animals[first_letter].append(animal)
                else:
                    sorted_animals[first_letter] = [sorted_animals[first_letter], animal]
            else:
                sorted_animals[first_letter] = animal
        return sorted_animals
    
    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("\nAnimal groups in", self.name + ":")
        for letter, animals in sorted_animals.items():
            print(f"{letter}: {animals}")

# instance
new_york_zoo = Zoo("Central Park Zoo")

# Add animals
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("Bear")
new_york_zoo.add_animal("Ape")
new_york_zoo.get_groups()