# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.


def function1():
    print("This function's here to call the 2nd one")
    function2()


def function2():
    name1=input("Enter your name: ")
    print("Hey, this is my Fuctions exercise, and your name is: ",name1)

function1()



#De acá para abajo no es parte del ejercicio, sólo estaba practicando lo de parámtros y con un ejercicio parecido al que explicó Alek en el video del material
def function3(parameter1,parameter2,parameter3="Solano"):
    print("Hello my name is ",parameter1,", my middle name is ",parameter2, ",and my lastname is ",parameter3)
    return parameter1, parameter2, parameter3

fullname=function3("Josue", "David")
print(fullname)
print(type(fullname))



list1=[1,3,4,5,6]
josue_score={"spanish":80, "math": 100, "english": 99}
paula_score={"spanish":60, "math": 90, "english": 69}

print(josue_score.get("spnish"))
print(list1[1])
def avarage_score(score):
    promedio=(score["spanish"]+score["math"]+score["english"])/3
    print (promedio)
    return 

avarage_score(josue_score)


# def average(score):
#     average_score=(score["spanish"]+score["math"]+score["english"]/3)
#     print (average_score)
#     return average_score

# average(josue_score)