""" 5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86. """


counter=0
listA=[]
while counter<10:
    number=int(input("Please type in a number: "))
    listA.append(number)
    counter=counter+1
print("The numbers you entered are: ",listA)
highest_number=max(listA)
print("The highest number out of the 10 values is: ",highest_number)

