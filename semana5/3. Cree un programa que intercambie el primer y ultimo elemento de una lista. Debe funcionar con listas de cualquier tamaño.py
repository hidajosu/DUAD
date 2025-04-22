""" 3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]` """

list1=["House","car","building"]
print("The list's contents are: ",list1)

def firsttolastandlasttofirst():
        list1[0], list1[-1] = list1[-1], list1[0]
        print("The new element order in the list is: ",list1)

firsttolastandlasttofirst()

#tengo que acotar que esto de "list1[-1] para llamar al último elemento de una lista, no se vio en la explicación ni tampoco el cómo hacer para intercambiar el orden de elementos como tal, esto lo tuve que buscar por fuera como tal"