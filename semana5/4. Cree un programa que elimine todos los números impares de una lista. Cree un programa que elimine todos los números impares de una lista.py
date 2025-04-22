""" # 4. Cree un programa que elimine todos los números impares de una lista.
#     1. Ejemplos:
#     2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]` """

list1=[1,2,5,6,3,7,4]
list2=[0]

for index in range(0,len(list1)):
    numero=list1[index]
    if numero%2==0:
        list2.append(numero)
print(list2)

#acá lo voy a intentar de otra forma, porque con toda honestidad me siento menos bruto con el ciclos WHILE que con ciclos FOR
listA=[1,2,3,4,5,6,7,8,9]
listB=[]
print(listA)

counter=0
while counter<len(listA):
    number2=listA[counter]
    if number2%2==0:
        listB.append(number2)
    counter=counter+1
print(listB)

deleteddata=listA.pop(0)
print(listA)


