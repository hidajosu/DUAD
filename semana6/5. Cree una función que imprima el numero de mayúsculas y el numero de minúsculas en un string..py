# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
#  """

def function1():
    phrase="ThIS Is a pHrasE wiTH UPPERCASE and lowercase LETTers"
    phrase=phrase.replace(" ","")
    counterupper=0
    counterlower=0
    for letter in phrase:
        if letter.upper():
            counterupper=counterupper+1
        else:
            counterlower=counterlower+1
    print("The amount of uppercase letters is: ",counterupper)
    print("The amount of lowercase letter is: ",counterlower)

function1()


def function2():
    phrase="ThIS Is a pHrasE wiTH UPPERCASE and lowercase LETTers"
    phrase=phrase.replace(" ","")
    counterupper2=0
    counterlower2=0
    for letter in phrase:
        if letter == letter.upper():
            counterupper2=counterupper2+1
        else:
            counterlower2=counterlower2+1
    print("The amount of uppercase letters is: ",counterupper2)
    print("The amount of lowercase letter is: ",counterlower2)

function2()

"""hola hola, mira, dejé ambas funciones porque necesito entender la diferencia entre la expreción
que está en el If de la primera con respecto al IF que está en la segunda...de hecho
la segunda función me salío de pura suerte inventando e inventando, pero con honestidad no les veo 
demasiada diferencia a lo que expresan ambos IFs, mas sí hay una diferencia sustancial, tal es así que con la expresión: "if letter == letter.upper():" sí funciona
el código (el objetivo del mismo al menos) y con la expresión: : "if letter.upper():" no funciona """
