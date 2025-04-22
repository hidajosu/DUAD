import random #Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

""" random_number= int(random.randint(0,10))
users_number=int(input('Guess the number: '))
while (random_number!=users_number):
    print("You haven't been able to guess the number, try again")
    users_number=int(input('Take a guess once more: '))
print("Congrats, you got it right!") """


ramdom_number=random.randint(0,10)
guess_the_number=int(input("Ingrese un número"))
while (ramdom_number!=guess_the_number):
    print("cromó")
    guess_the_number=int(input("Ingrese un número"))
print("adivinó el número")