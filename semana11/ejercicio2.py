# 2. Cree una clase de `Bus` con:
#     1. Un atributo de `max_passengers`.
#     2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#     3. Un método para bajar pasajeros uno por uno (en cualquier orden).



class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(person.name," has boarded the bus")
        else:
            print("The bus is full. No more passengers can be added")

    def remove_passenger(self, person_name):
        for passenger in self.passengers:
            if passenger.name == person_name:
                self.passengers.remove(passenger)
                print(person_name," has left the bus")
                return
        print("No passenger named",person_name,"found on the bus")

if __name__ == "__main__":
    bus = Bus(max_passengers=30)
    person1 = Person("Alice")
    person2 = Person("Bob")

    bus.add_passenger(person1)
    bus.add_passenger(person2)
    bus.remove_passenger("Alice")
    bus.remove_passenger("Charlie")