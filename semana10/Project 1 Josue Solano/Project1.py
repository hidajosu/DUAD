# # Requerimientos

# Cree un programa tener tenga una interfaz por linea de comando (es decir, a base de `inputs` y `prints`). Este debe tener un menu que me permita accesar a todas las funciones (**deberá validar que se ingrese una opción del valida del menú**):

# 1. Ingresar información de `n` cantidad de estudiantes, *uno por uno*.
#     1. Cada estudiante debe incluir:
#         1. Nombre completo
#         2. Sección (ejemplo: *11B*)
#         3. Nota de español
#         4. Nota de inglés
#         5. Nota de sociales
#         6. Nota de ciencias
#     2. Deberá validar que las notas ingresadas sean validas (números de 0 a 100) y seguir pidiéndola hasta que sea valida.
# 2. Ver la información de todos los estudiantes ingresados.
# 3. Ver el top 3 de los estudiantes con la mejor nota promedio (*es decir, el promedio de su* `nota de español`+ `nota de inglés` + `nota de sociales` + `nota de ciencias`).
# 4. Ver la nota promedio entre las notas de todos los estudiantes (es decir, el promedio del `promedio de notas` *de cada uno*). 
# 5. Exportar todos los datos actuales a un archivo CSV.
# 6. Importar los datos de un archivo CSV previamente exportado.
#     1. Si no hay un archivo previamente exportado, debe de decírselo al usuario.

# ---

# Divida el proyecto en los siguientes módulos:

# - `main`: tendrá el punto de entrada del programa.
# - `menu`: tendrá toda la lógica relacionada al menu de opciones.
# - `actions`: tendrá toda la lógica de las acciones del menu, excepto las de exportar e importar datos.
# - `data`: tendrá toda la lógica de exportación e importación de datos


print("""--------------------------Welcome to your grading assiting program--------------------------
This tool is aimed to help you managing your students' grades for a series of subjects, among them:
-->Spanish
-->English
-->Social Studies
-->Science
      
      
Let's begin by entering the amount of students you'd like to enter the information for\n\n\n""")


def number_students():
    global amount_students
    amount_students=input("Enter the number of students you'd like to enter data for: ")
    if amount_students.isdigit():
        amount_students=int(amount_students)
        print("The entered amount of students to enter data for is: ",amount_students)
    else:
        print("Incorrect data entered, try again")
        number_students()
        

def student_name():
    global name,dictname
    name=input("Enter the student's name: ")
    if name.isdigit():
        print("Incorrect data entered, try again")
        student_name()
    else:
        print("The entered name is: ",name)
        dictname={"Student's name":name}  


def class_number():
    global classID,dictclassID
    classID=input("Enter the student's class ID (for examplo 11B): ")
    if classID.isdigit():
        print("Incorrect data entered, the class ID needs to contain numbers and letter and cannot surpass 3 characters, try again")
        class_number()
    elif len(classID)!=3:
        print("Incorrect data entered, the class ID needs to contain numbers and letter and cannot surpass 3 characters, try again")
        class_number()
    else:
        print("The entered class ID is: ",classID)
        dictclassID={"Student's Class ID":classID}      


def grade_spanish():
    global spanish,dictspanish
    spanish=input("Enter the grade for the student's Spanish grade: ")
    if spanish.isdigit():
        spanish=int(spanish)
        if spanish==0 or spanish<=100:
            print("The entered grade for Spanish: ",spanish)
            dictspanish={"Spanish grade":spanish}
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_spanish()
    else:
        print("Incorrect data entered, only numerical info is accepted")
        grade_spanish()


def grade_english():
    global english,dictenglish
    english=input("Enter the grade for the student's English grade: ")
    if english.isdigit():
        english=int(spanish)
        if english==0 or english<=100:
            print("The entered grade for English: ",english)
            dictenglish={"English grade":english}
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_english()
    else:
        print("Incorrect data entered, try again")
        grade_english()


def grade_social():
    global social, dictsocial
    social=input("Enter the grade for the student's Social Studies grade: ")
    if social.isdigit():
        social=int(social)
        if social==0 or social<=100:
            print("The entered grade for Social Studies: ",social)
            dictsocial={"Social Studies grade":social}
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_social()
    else:
        print("Incorrect data entered, try again")
        grade_social()


def grade_science():
    global science,dictscience
    science=input("Enter the grade for the student's Science grade: ")
    if science.isdigit():
        science=int(science)
        if science==0 or science<=100:
            print("The entered grade for Science: ",science)
            dictscience={"Science grade":science}
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_science()
    else:
        print("Incorrect data entered, try again")
        grade_science()


def average():
        global avarage_grade_individual,dictavarage, global_avarage, top3
        avarage_grade_individual=(spanish + english + science + social) /4
        dictavarage= {"Avarage score for this student's grades": avarage_grade_individual}
        global_avarage=0
        counter=0
        while counter<amount_students:
            global_avarage=avarage_grade_individual+global_avarage
            counter=counter+1
        global_avarage=global_avarage/amount_students
        counter2=0
        while counter2<amount_students:
            top3=[]
            top3.append(avarage_grade_individual)
            counter2=counter2+1
        top3.sort()


def data_introduction():
    global student_info
    global globalList
    globalList=[]
    counter3=0
    while counter3 < amount_students:
        student_name()
        class_number()
        grade_spanish()
        grade_english()
        grade_social()
        grade_science()
        student_info=[dictname,dictclassID,dictspanish,dictenglish,dictsocial,dictscience,dictavarage]
        globalList.append(student_info)
        counter3=counter3+1


def menu():
    print("""Enter the a valid number from 1 to 6 to perform a desired task:
          
          1-->Enter the information about the students you want to record data for
          2-->Show the entered information
          3-->Show the top 3 students with the best avarage grades 
          4-->Show the average of the avarage grades from all the students
          5-->Export all entered data to a CSV file
          6-->Import data from a CSV file which was exported beforehand using the program (if there's no previouly uploaded file, the program will let you know about this)


          """)
    options=input("Enter your desired option: ")
    if options.isdigit():
        match options:
            case 1:
                number_students()
                data_introduction()
                menu()
            case 2:
                print("The entered data is: ", globalList)
                menu()
            case 3:
                print("As per the chosen option, you wish to see the top 3 avarage scores from the analized students, these avarage scores are: ",top3[0]," ",top3[1]," ",top3[2])
                menu()
            case 4:
                print("As per your chosen option, you wish to see the average of the avarage grades from all the students\nThis value is: ",global_avarage)
                menu()
                

menu()       


# 4. Ver la nota promedio entre las notas de todos los estudiantes (es decir, el promedio del `promedio de notas` *de cada uno*). 
# 5. Exportar todos los datos actuales a un archivo CSV.
# 6. Importar los datos de un archivo CSV previamente exportado.
#     1. Si no hay un archivo previamente exportado, debe de decírselo al usuario.
