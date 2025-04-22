#Cree un programa que le pida tres números al usuario y muestre el mayor.

numero1=int(input("Enter the 1st out of 3 numbers "))
numero2=int(input("Enter the 2nd out of 3 numbers "))
numero3=int(input("Enter the 3rd out of 3 numbers "))
mayor_número=max(numero1,numero2,numero3)
print('The highest number out of the 3 you entered is: ',mayor_número)