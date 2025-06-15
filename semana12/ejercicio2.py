# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos 
#     de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de 
#     `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para 
#     poder calcular el área y el perímetro.


# Ejercicio 2
# ✨ Detalles a mejorar:

# Uso de métodos abstractos:
# Aunque la clase Shape hereda de ABC, los métodos calculate_area 
# y calculate_perimeter no están decorados con @abstractmethod.
# → Esto es importante para asegurarse de que las clases hijas 
# implementen obligatoriamente esos métodos.

# Input en definición de clase:
# Los valores se están solicitando con input() dentro del cuerpo de las clases.
# → Esto hace que los valores sean globales en la clase y 
# compartidos por todas las instancias. 
# Además, no es recomendable que una clase dependa de entradas 
# de usuario directamente en su definición.

# Uso de self y init:
# En lugar de declarar radius, side1, etc., como variables dentro de la clase, 
# deberías asignarlos como atributos dentro del init.
# → Esto permite que cada instancia de figura 
# tenga sus propios datos y mejora el diseño orientado a objetos.


import math
from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        print("The inputed radius was: ", self.radius,"cm")


    def calculate_perimeter(self):
        peri=(2*self.radius)*math.pi
        print("The circle's perimeter is: ",peri,"cm")


    def calculate_area(self):
        area=(self.radius*self.radius)*math.pi
        print("The circle's area is: ",area,"cm2")


class Rectangle(Shape):
    def __init__(self, side1,side2):
        self.side1=side1
        self.side2=side2
        print("The inputed rectangle's longest side side was: ",side1,"cm")
        print("The inputed rectangle's shortest side side was: ",side2,"cm")

    def calculate_perimeter(self):
        peri=(2*self.side1)+(2*self.side2)
        print("The rectangle's perimeter is: ",peri,"cm")


    def calculate_area(self):
        area=(self.side1*self.side2)
        print("The rectangle's area is: ",area,"cm2")



class Square(Shape):
    def __init__(self, side):
        self.side=side
        print("The inputed square's side was: ",side,"cm")

    def calculate_perimeter(self):
        peri=self.side*4
        print("The square's perimeter is: ",peri,"cm")


    def calculate_area(self):
        area=(self.side*self.side)
        print("The square's area is: ",area,"cm2")        

shape1=Circle(3)
shape1.calculate_perimeter()
shape1.calculate_area()

shape2=Rectangle(10,9)
shape2.calculate_perimeter()
shape2.calculate_area()

shape3=Square(4)
shape3.calculate_perimeter()
shape3.calculate_area()