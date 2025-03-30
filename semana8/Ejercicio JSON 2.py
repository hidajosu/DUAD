# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

with open("yeison.json", "r") as f1:
    f1=f1.read()
    print("The current pokemon's info is: ",f1)
    print(type(f1))
    f1=json.loads(f1)
    print(type(f1))
    
# f2=json.dumps(f)
# print(type(f2))

name=input("Enter the new pokemon you'd like to add: ")
type=input("Enter the type of the pokemon you'd like add: ")
hp=input("Enter the hp of the pokemon you'd like to add: ")
attack=input("Enter the attack value of the pokemon you'd like to add: ")
defense=input("Enter the defense value of pokemon you'd like to add: ")
spattack=input("Enter the SP Attack value of the new pokemon you'd like to add: ")
spdefense=input("Enter the SP Defense value of the new pokemon you'd like to add: ")
speed=input("Enter the speed value of the new pokemon you'd like to add: ")

list2=[{"name": {"english": name},"type": [type],"base": {"HP": hp,"Attack": attack ,"Defense": defense,
      "Sp. Attack": spattack,"Sp. Defense": spdefense,"Speed": speed}}]
print("The new pokemon related information you'd like to add is: ", list2)

list2.extend(f1) #porque si f1 es una lista (según el print(type(XXXX), no puede hacer un f1.append/extend/insert)
print(list2)
# print(type(list2)) #porqué esto me da error? O sea, porqué no me deja pedir el type de list2...yo sé que es una lista pero sólo quiero confirmar que así sea
# list2.insert(0,f1)
list2=json.dumps(list2)

with open("yeison2.json", "w") as f3:
    f3.write(list2)