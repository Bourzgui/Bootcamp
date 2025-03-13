import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        """Initialise la classe Circle avec le rayon ou le diamètre."""
        if radius:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")
    
    def area(self):
        """Calcule et retourne l'aire du cercle."""
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        """Retourne une chaîne de caractères qui représente le cercle."""
        return f"Circle(radius={self.radius}, diameter={self.diameter})"
    
    def __repr__(self):
        """Retourne une représentation officielle du cercle."""
        return self.__str__()

    def __add__(self, other):
        """Additionne deux cercles en ajoutant leurs rayons et retourne un nouveau cercle."""
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        return NotImplemented
    
    def __gt__(self, other):
        """Comparaison de taille des cercles en fonction du rayon, retourne un booléen."""
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    
    def __eq__(self, other):
        """Vérifie si deux cercles sont égaux (même rayon), retourne un booléen."""
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented
    
    def __lt__(self, other):
        """Comparaison de taille des cercles en fonction du rayon, retourne un booléen."""
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

 
def draw_circle(circle):
    turtle.penup()
    turtle.goto(0, -circle.radius * 10)  
    turtle.pendown()
    turtle.circle(circle.radius * 10)   
    turtle.penup()
    turtle.goto(0, 0)

def draw_sorted_circles(circles):
    turtle.speed(1)
    for circle in circles:
        draw_circle(circle)
    turtle.done()

circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)

print(circle1)   
print(circle2)   
 
print(f"Area of circle1: {circle1.area()}")  
print(f"Area of circle2: {circle2.area()}")   
 
circle3 = circle1 + circle2
print(f"New circle after addition: {circle3}")  
 
print(circle1 > circle2)   
print(circle2 > circle1)   
print(circle1 == circle2)   

circles = [Circle(radius=4), Circle(radius=7), Circle(radius=2)]
circles.sort()   
print(f"Sorted circles: {circles}")
 
draw_sorted_circles(circles)
