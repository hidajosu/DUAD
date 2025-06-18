#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

"""Esto tiene que ver con el ejemplo de Superman que Alex puso en la teoría. La herencia
multiple permite mezclar comportamientos de diferentes clases y así 
crear nuevas clases que combinen varias capacidades (por ejemplo, lo de superman del
ejemplo, que puede caminar, volar y correr"""


class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()   
duck.swim()