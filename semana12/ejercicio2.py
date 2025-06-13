# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

import math
from abc import ABC, abstractmethod

class Shape (ABC):
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Circle(Shape):
    radius=int(input("What's the radius of the circle (in cm)?: "))
    print("The inputed radius was: ",radius,"cm")

    def calculate_perimeter(self):
        peri=(2*self.radius)*math.pi
        print("The circle's perimeter is: ",peri,"cm")


    def calculate_area(self):
        area=(self.radius*self.radius)*math.pi
        print("The circle's area is: ",area,"cm2")


class Rectangle(Shape):
    side1=int(input("What's the rectangle's longest side (in cm)?: "))
    print("The inputed rectangle's longest side side was: ",side1,"cm")

    side2=int(input("What's the rectangle's shortest side (in cm)?: "))
    print("The inputed rectangle's shortest side side was: ",side2,"cm")

    def calculate_perimeter(self):
        peri=(2*self.side1)+(2*self.side2)
        print("The rectangle's perimeter is: ",peri,"cm")


    def calculate_area(self):
        area=(self.side1*self.side2)
        print("The rectangle's area is: ",area,"cm2")



class Square(Shape):
    side=int(input("What's the square's side (in cm)?: "))
    print("The inputed square's side was: ",side,"cm")

    def calculate_perimeter(self):
        peri=self.side*4
        print("The square's perimeter is: ",peri,"cm")


    def calculate_area(self):
        area=(self.side*self.side)
        print("The square's area is: ",area,"cm2")        

shape1=Circle()
shape1.calculate_perimeter()
shape1.calculate_area()

shape2=Rectangle()
shape2.calculate_perimeter()
shape2.calculate_area()

shape3=Square()
shape3.calculate_perimeter()
shape3.calculate_area()