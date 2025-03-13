class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Félicitations ! {kwargs['name']} est né dans la famille {self.last_name}.")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False  # Si le membre n'existe pas

    def family_presentation(self):
        print(f" Famille {self.last_name}:")
        for member in self.members:
            print(f"  - {member['name']}, {member['age']} ans, {member['gender']}")


class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] < 18:
                    raise Exception(f"{name} est trop jeune pour utiliser son pouvoir !")
                print(f" {name} utilise son pouvoir : {member['power']} !")
                return
        print(f" {name} n'est pas dans la famille.")

    def incredible_presentation(self):
        print("\n* Voici notre famille INCROYABLE ! *")
        super().family_presentation()
        for member in self.members:
            print(f"  Super-héros: {member['incredible_name']}, Pouvoir: {member['power']}")
incredibles_family = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])
incredibles_family.incredible_presentation()
try:
    incredibles_family.use_power("Michael")
    incredibles_family.use_power("Sarah")
except Exception as e:
    print(e)
incredibles_family.born(name="Jack", age=1, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")

incredibles_family.incredible_presentation()
