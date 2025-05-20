# 1. Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

import math

class Circle:
    radius=10
    def get_area(self):
        print("We are now proceeding to obtain the area")
        area=self.radius*(math.pi*math.pi)
        print("The area is: ",area,"cm2")

circle1= Circle()
circle1.get_area()

