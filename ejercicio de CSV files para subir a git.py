
""" 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB
    2. Ejemplo de archivo final: """

import csv
import json

my_dict_for_info={}
headers_for_dict=["marca","modelo","año","km","dekra"]

with open(r"C:\Users\hidajosu\Desktop\ejercicio de CSV files para subir a git.csv", "w", encoding="utf-8", newline="")as file:
    write=csv.DictWriter(file,fieldnames=headers_for_dict)
    write.writeheader()
    write.writerow(my_dict_for_info)

def main():
    desicion=input("Quiere meter más info al diccionario?: ")
    desicion=desicion.lower()
    desicion=desicion.replace(" ","")
    while desicion=="si":
        enter_info()
        desicion=input("Quiere meter más info al diccionario?: ")
        desicion=desicion.lower()
        desicion=desicion.replace(" ","")
    if desicion=="no":
        show_info()
    else:
        print("Opción incorrecta, intente de nuevo")
        main()
    
def enter_info():
    marca=input("Cuál es la marca del carro?: ")
    modelo=input("Qué modelo de carro es?: ")
    año=input("Qué año es el carro?: ")
    km=input("Qué KM tiene el carro?: ")
    dekra=input("El carro tiene DEKRA?: ")
    my_dict_for_info["marca"]=marca
    my_dict_for_info["modelo"]=modelo
    my_dict_for_info["año"]=año
    my_dict_for_info["km"]=km
    my_dict_for_info["dekra"]=dekra
    add_info_to_file()
    
    

def add_info_to_file():
    with open (r"C:\Users\hidajosu\Desktop\ejercicio de CSV files para subir a git.csv", "a", encoding="utf-8", newline="") as file:
        write=csv.DictWriter(file, fieldnames=headers_for_dict)
        write.writerow(my_dict_for_info)

def show_info():
    with open(r"C:\Users\hidajosu\Desktop\ejercicio de CSV files para subir a git.csv", "r", encoding="utf-8",) as file:
        read=csv.DictReader(file)
        for line in read:
            print(line)

main()
