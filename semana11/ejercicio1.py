# 1. Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

"""• En el ejercicio del círculo, te sugerimos mover 
el atributo radius al constructor (__init__) 
y corregir la fórmula del área para que dependa
del radio y no del cuadrado de pi.
"""

import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        print("We are now proceeding to obtain the area")
        area=self.radius*(math.pi**2)
        print("The area is: ",area,"cm2")


def get_radius():
    while True:
        radius_value = input("Enter the value for the radius of the circle (numbers only): ")
        try:
            radius_value = float(radius_value)
            if radius_value > 0:
                print("The entered value for the radius is:", radius_value)
                return radius_value
            else:
                print("Radius must be positive. Try again.")
        except ValueError:
            print("The entered value isn't valid, try again.")

circle_value=get_radius()
print(type(circle_value))
circle1= Circle(circle_value)
circle1.get_area()
