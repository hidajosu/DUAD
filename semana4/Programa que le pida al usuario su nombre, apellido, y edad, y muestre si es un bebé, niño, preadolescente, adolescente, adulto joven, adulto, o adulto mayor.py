#Haga programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, adolescente, adulto joven, adulto, o adulto mayor.

name=input("Enter your full name: ")
age=int(input("What's your age? "))
if(age<3):
    print("The person named ",name, "is ",age, " years old and that makes him/her a baby")
elif(age>=3 and age<=10):
    print("The person named ",name, "is ",age, " years old and that makes him/her a toddler")
elif(age>10 and age<=18):
    print("The person named ",name, "is ",age, " years old and that makes him/her a teenager")
elif(age>18 and age<=35):
    print("The person named ",name, "is ",age, " years old and that makes him/her a young adult")
elif(age>35 and age<=60):
    print("The person named ",name, "is ",age, " years old and that makes him/her an adult")
else:
    print("The person named ",name, "is ",age, " years old and that makes him/her an elderly person")
