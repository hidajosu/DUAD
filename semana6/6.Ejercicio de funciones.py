# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def function1():
    string1=input("enter a phrase in which each word is separated with a '-': ")
    list1=string1.split("-")
    list1.sort()
    print(list1)
    string1=" ".join(list1)
    string1=string1.replace(" ","-")
    print("The sequence of words you entered alphabetically arranged is: ",string1)

function1()
