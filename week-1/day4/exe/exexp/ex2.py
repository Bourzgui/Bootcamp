class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if my_strength > other_strength:
            return f"{self.name} wins the fight!"
        elif my_strength < other_strength:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Rocky", 4, 30)

print(dog1.bark())  
print(dog2.run_speed())  
print(dog1.fight(dog3))  

 
