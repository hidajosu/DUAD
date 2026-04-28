text="Lo que está para meter en un file"

print(text)

def meter_en_file(path):
    with open(path,"w",encoding="utf-8") as file:
        texto= text
        print(file.write(texto))

def leer_file(path):
    with open(path,"r",encoding="utf-8") as file:
        print(file.read())

meter_en_file(r"C:\Users\hidajosu\Desktop\i'm back")
leer_file(r"C:\Users\hidajosu\Desktop\i'm back")

class Carro():
    marca="Toyota"
    def __init__(self, modelo, año, cantidad_puertas,transmision,motor):
        self.modelo=modelo
        self.año=año
        self.cantidad_puertas=cantidad_puertas
        self.transmision=transmision
        self.motor=motor

Tacoma=Carro("Tacoma", 2026, 4, "Automática", "2400CC")
print(Tacoma.motor)
Sequoia=Carro("Sequoia", 2026, 5, "Automática", "3500CC")
print(Sequoia.motor)

class Carro2(Carro):
    marca="Lexus"

IS250=Carro2("IS250", 2026, 4, "Automática", "2500CC")
print(IS250.marca)
print(IS250.motor)
print(Sequoia.transmision)
