# Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


def open_file(x):
    with open(x, "r") as file1:
        global lines
        lines=file1.read()
        lines=lines.split("\n")
        lines.sort()
        print(lines)

open_file("Songs2.txt")

with open("Songs3.txt", "w") as file2:
    file2.write
    
i=0
while i<len(lines):
    with open("Songs3.txt", "a") as file3:
        file3.write(lines[i] + ", ")
        i=i+1

#sé que esto es lo mismo que el ciclo anterior pero es para practicar ambos tipos de ciclos
for i in range(0,len(lines)):
    with open("Songs3.txt", "a") as file3:
        file3.write(lines[i] + ", ")





