""" 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util """

list1=["Hello", "Josue Solano","31"]
list2=["my name is","and I'm", "years old"]

counter=0
while counter<len(list1):
    print(list1[counter])
    print(list2[counter])
    counter=counter+1    