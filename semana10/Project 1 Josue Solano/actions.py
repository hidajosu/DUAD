globalList=[]


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
        try: 
            avarage_grade_individual=(spanish + english + science + social) /4
            dictavarage= {"Avarage score for this student's grades": avarage_grade_individual}
            global_avarage=0
            counter=0
            while counter<amount_students:
                global_avarage=avarage_grade_individual+global_avarage
                counter=counter+1
            global_avarage=global_avarage/amount_students
            top3=[]
            counter2=0
            while counter2<amount_students:
                top3.append(avarage_grade_individual)
                counter2=counter2+1
            top3.sort()

        except IndexError as error:
            print("There was an error: ", error)

globalList=[]

def data_introduction():
    global student_info
    counter3=0
    while counter3 < amount_students:
        student_name()
        class_number()
        grade_spanish()
        grade_english()
        grade_social()
        grade_science()
        average()
        student_info=[dictname,dictclassID,dictspanish,dictenglish,dictsocial,dictscience,dictavarage]
        globalList.append(student_info)
        counter3=counter3+1
    print(globalList)