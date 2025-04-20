import csv

print("""--------------------------Welcome to your grading assiting program--------------------------
This tool is aimed to help you managing your students' grades for a series of subjects, among them:
-->Spanish
-->English
-->Social Studies
-->Science
      
      
Let's begin by entering the amount of students you'd like to enter the information for\n\n\n""")

globaldata=[]
print(type(globaldata))

def number_students():
    amount_students=input("Enter the number of students you'd like to enter data for: ")
    if amount_students.isdigit():
        amount_students=int(amount_students)
        print("The entered amount of students to enter data for is: ",amount_students)
        return amount_students
    else:
        print("Incorrect data entered, try again")
        number_students()
        

def student_name():
    name=input("Enter the student's name: ")
    if name.isdigit():
        print("Incorrect data entered, try again")
        student_name()
    else:
        print("The entered name is: ",name)
        return name


def class_number():
    classID=input("Enter the student's class ID (for example 1234): ")
    if len(classID)==4 and classID.isdigit():
        print("The entered Class ID is: ", classID)
        return classID
    else:
        print("The Class ID you entered isn't valid, try again. Keep in mind that this ID can only have numbers and needs to be composed by 4 digits")
        class_number()
   

def grade_spanish():
    spanish=input("Enter the grade for the student's Spanish grade: ")
    if spanish.isdigit():
        spanish=int(spanish)
        if spanish==0 or spanish<=100:
            print("The entered grade for Spanish: ",spanish)
            return spanish
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_spanish()
    else:
        print("Incorrect data entered, only numerical info is accepted")
        grade_spanish()


def grade_english():
    english=input("Enter the grade for the student's English grade: ")
    if english.isdigit():
        english=int(english)
        if english==0 or english<=100:
            print("The entered grade for English: ",english)
            return english
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_english()
    else:
        print("Incorrect data entered, try again")
        grade_english()


def grade_social():
    social=input("Enter the grade for the student's Social Studies grade: ")
    if social.isdigit():
        social=int(social)
        if social==0 or social<=100:
            print("The entered grade for Social Studies: ",social)
            return social
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_social()
    else:
        print("Incorrect data entered, try again")
        grade_social()


def grade_science():
    science=input("Enter the grade for the student's Science grade: ")
    if science.isdigit():
        science=int(science)
        if science==0 or science<=100:
            print("The entered grade for Science: ",science)
            return science
        else:
            print("The grade can't be lower than 0 or higher than 100")
            grade_science()
    else:
        print("Incorrect data entered, try again")
        grade_science()


def individual_average():
        avarage_grade_individual=(grade_spanish()+grade_english()+grade_social()+grade_science())/4
        return avarage_grade_individual

        
    
def global_average():
        g_avarage=0
        counter=0
        while counter<number_students():
            g_avarage=g_avarage+individual_average()
            counter=counter+1
        g_avarage=g_avarage/4
        print("The avarage grade of all the students' grades (the avarage score of the the avarage scores) is: ", g_avarage)
        return g_avarage




        try: 
            avarage_grade_individual=(grade_spanish()+grade_english()+grade_social()+grade_science()) /4
            global_avarage=0
            counter=0
            n_students=number_students()
            while counter<n_students:
                global_avarage=avarage_grade_individual+global_avarage
                counter=counter+1
            global_avarage=global_avarage/n_students
            top3=[]
            counter2=0
            while counter2<n_students:
                top3.append(avarage_grade_individual)
                counter2=counter2+1
            top3.sort()

        except IndexError as error:
            print("There was an error: ", error)
        

def data_introduction():
    global globaldata
    counter3=0
    n_students=number_students()
    top_scores=[]
    g_avarage=0
    while counter3 < n_students:
        s_name = student_name()
        c_number = class_number()
        g_spanish = grade_spanish()
        g_english = grade_english()
        g_social = grade_social()
        g_science = grade_science()
        avarage_grade_individual=(g_spanish+g_english+g_social+g_science)/4
        top_scores.append(avarage_grade_individual)
        g_avarage=avarage_grade_individual+g_avarage
        student_info={"Student's name": s_name, "Student's Class ID": c_number, "Spanish grade": g_spanish, "Englisgh grade": g_english, "Social Studies grade": g_social, "Science grade": g_science, "Avarage score for this student's grades": avarage_grade_individual, "Avarage score for all student's grades": g_avarage}
        print(type(student_info))
        globaldata.append(student_info)
        counter3=counter3+1
    print(type(globaldata))
    print(globaldata)
    top_scores.sort()
    g_avarage=g_avarage/n_students
    print("The avarage of the avarage scores is: ",g_avarage)
    return g_avarage, top_scores




    # headers = ("Name", "Student's Class ID", "Spanish", "English grade", "Social Studies grade", "Science grade", "Avarage score for this student's grades")
    # with open("scores.csv", mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(globalList)
        


def data_export():
    import csv
    global headers
    if len(globaldata)==0:
        print("We can't export nothing yet since no data has been entered yet, please proceed to enter data so it can later be saved and exported")
    else:
        headers=("Name", "Student's Class ID", "Spanish", "English grade", "Social Studies grade", "Science grade", "Avarage score for this student's grades")
        with open("Score file.csv", "a", encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerows(globaldata)


def data_import():
    import csv
    global headers
    if len(globalList)==0:
        print("We can't import nothing yet since no data has been exported to beging with, please proceed to enter data so it can later be saved and exported, and then so it can be imported")
    else:
        with open("Score file.csv", "r", encoding="utf-8") as file:
            csv.reader=csv.reader(file)
            



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
    try:
        if options.isdigit():
            options=int(options)
            match options:
                case 1:
                    data_introduction()
                    menu()
                case 2:
                    print("The entered data is: ", globaldata)
                    menu()
                case 3:
                    print("As per the chosen option, you wish to see the top 3 avarage scores from the analized students, these avarage scores are: ",top3[0],top3[1],top3[2])
                    menu()
                case 4:
                    print("As per your chosen option, you wish to see the average of the avarage grades from all the students\nThis value is: ", )
                    menu()
                case 5:
                    print("As per your chosen option, you wish to export the information into an CSV file")
                    data_export()
                    menu()
                case 6:
                    print("As per your chosen option, you wish to import the information you had sent to the CSV file")
                    data_import()
                    menu()
                case 7:
                    print("As per your chosen option, you wish to get out of the program, thanks for using our system, bye")
                case _:
                    print("You entered an invalid entry, try again")
                    menu()
        else:
            print("You entered an invalid entry, try again")
            menu()
    except Exception as error:
        print("There was an error: ",error)
        menu()           

menu()
    


# 4. Ver la nota promedio entre las notas de todos los estudiantes (es decir, el promedio del `promedio de notas` *de cada uno*). 
# 5. Exportar todos los datos actuales a un archivo CSV.
# 6. Importar los datos de un archivo CSV previamente exportado.
#     1. Si no hay un archivo previamente exportado, debe de decírselo al usuario.
