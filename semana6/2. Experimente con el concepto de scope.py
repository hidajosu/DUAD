# 2. Experimente con el concepto de scope:
#-->Intente accesar a una variable definida dentro de una función desde afuera.
#-->Intente accesar a una variable global desde una función y cambiar su valor.

"""Se me indicó esto en Notion: Dentro de una función, vas a crear una variable, 
la que usted guste, por ejemplo, num1 = 2, ahora, afuera de 
este método o función vas a intentar cambiar la variable que 
creaste adentro del método, a ver que te logra imprimir """

def function11(): # acá estoy creando la función y le voy a decir al usuario que ingrese el valor de la variable
    numx=int(input("Digite un número"))
    print(numx)
    return numx #acá estoy pidiendole que retorne ese valor, pero como está dentro de la función, se queda dentro de la función, si yo intento llamarla fuera de la misma, no será reconocida

"""function11()
print(numx)
numx=numx+2 esto me va a dar error porque en la realidad "numx" no existe sino dentro de la función
 """
numx=function11() #lo único que se me ocurre es llamarla así (porque se me dijo que no se puede usar el keyword "global" dentro de la función original
numx=numx+2
print(numx)