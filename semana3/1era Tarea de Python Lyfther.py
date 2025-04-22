print("Esta es la primer tarea relacionada a Python de la academia Lifter\nVoy a aprovechar este file para mostrar los 2 ejercicios asignados:\n-Use la función print() para mostrar distintos textos en pantalla\n-Use la función print() para mostrar resultados de operaciones matemáticas básicas (+,-,/,*)")
numero1=input("Digite el primer número ")
numero2=input("Digite el segundo número ")
if(numero1.isdigit() and numero2.isdigit()):
    numero1=float(numero1)
    numero2=float(numero2)
else:print("No digitó valores numéricos con los que se puedan hacer operaciones matemáticas")
operacionDeseada=int(input("Digite 1 si quiere sumar los valores entre sú, un 2 si quiere restarle al numero 1 el numero 2, un 3 si quiere restarle al numero 2 el numero 1, un 4 si quiere multiplicar los numeros entre sí, un 5 si quiere dividir el numero 1 entre el numero 2 o un 6 si quiere dividir el numero 2 entre el numero 1 "))
if(operacionDeseada==1):
    suma=numero1+numero2
    print("El resultado de la suma es de: ",suma)
elif(operacionDeseada==2):
    resta=numero1-numero2
    print("El resultado de la resta es de: ",resta)
elif(operacionDeseada==3):
    resta=numero2-numero1
    print("El resultado de la resta es de: ",resta)
elif(operacionDeseada==4):
    multiplicacion=numero1*numero2
    print("El resultado de la multiplicación es de: ",multiplicacion)
elif(operacionDeseada==5):
    division=numero1/numero2
    print("El resultado de la división es de: ",division)
elif(operacionDeseada==6):
     division=numero2/numero1
     print("El resultado de la división es de: ",division)
else:
    print("No digitó un número válido para indicar una operación matemática")