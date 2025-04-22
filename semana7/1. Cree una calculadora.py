# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


current_number = 0
print(current_number)
    

def sum():
    try:
        global current_number
        new_number=input("Enter the number you'd like to add up to the current number")
        if new_number.isdigit():
            new_number=int(new_number)
            try:
                current_number=current_number+new_number
                print(current_number)
                options()
            except ValueError as error:
                print("You entered an invalid value: ", error)
                sum()
        else:
            print("The value entered isn't valid")
            print(current_number)
            sum()
    except Exception as error:
            print("Something is off, try again")
            sum()


def substraction():
    try:
        global current_number
        new_number=input("Enter the number you'd like to subtract from the current value")
        if new_number.isdigit():
            new_number=int(new_number)
            try:
                current_number=current_number-new_number
                print(current_number)
                options()
            except ValueError as error:
                print("You entered an invalid value: ", error)
                substraction()
        else:
            print("The value entered isn't valid")
            print(current_number)
            substraction()
    except Exception as error:
            print("Something is off, try again")
            substraction()


def multiplication():
    try:
        global current_number
        new_number=input("Enter the number you'd like to multiply the current number by")
        if new_number.isdigit():
            new_number=int(new_number)
            try:
                current_number=current_number*new_number
                print(current_number)
                options()
            except ValueError as error:
                print("You entered an invalid value: ", error)
                multiplication()
        else:
            print("The value entered isn't valid")
            print(current_number)
            substraction()
    except Exception as error:
        print("Something is off, try again")
        multiplication()


def division():
    try:
        global current_number
        new_number=input("Enter the number you'd like to divide the current number by")
        if new_number.isdigit():
            new_number=int(new_number)
            try:
                current_number=current_number/new_number
                print(current_number)
                options()
            except ValueError as error:
                print("You entered an invalid value: ", error)
                division()
        else:
            print("The value entered isn't valid")
            print(current_number)
            division()
    except Exception as error:
        print("Something is off, try again")
        division()


def erase():
    global current_number
    current_number=0
    print(current_number)
    options()


def options():
    option=input("""Enter one of the following numbers to choose your option:
                    1->Sum
                    2->Substraction
                    3->Mutliplication
                    4->Division
                    5->Erase result
                    Enter your option: """)
    if(option.isdigit()):
        try:
            option=int(option)
            match option:
                case 1: 
                    sum()
                case 2:
                    substraction()
                case 3: 
                    multiplication()
                case 4:
                    division()
                case 5:
                    erase()
                case _:
                    print("You didn't enter a valid entry")
                    options()
        except UnboundLocalError as error:
            print("You didn't enter a valid value, here's your error: ",error)
            options()

    else:
        print("You did not enter a number, try again")
        options()

options()
