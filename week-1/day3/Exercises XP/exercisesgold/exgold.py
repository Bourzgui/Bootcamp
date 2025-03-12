import random

class Circle:
    def __init__(self, radius=1.0):
        if radius <= 0:
            raise ValueError("Le rayon doit être positif.")
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def definition(self):
        print("Un cercle est une forme dont tous les points sont à égale distance de son centre.")


mon_cercle = Circle(3)

print(f"Périmètre du cercle : {mon_cercle.perimeter():.2f}")
print(f"Surface du cercle : {mon_cercle.area():.2f}")
mon_cercle.definition()
