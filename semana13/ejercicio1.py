def print_params_and_return(func):
    def wrapper(*args):
        print("Function parameters:", args)
        result = func(*args)
        print("Function return:", result)
        return result
    return wrapper

@print_params_and_return
def inifite_para(*args):
    suma_total = 0
    for i in args:
        print("This parameter's value is:", i)
        suma_total = suma_total + i
    print("La suma total de los valores es: ", suma_total)
    return suma_total

inifite_para(1, 2, 3, 4, 45, 6, 7, 6)


