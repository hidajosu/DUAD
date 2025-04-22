def add_student(students):
    print("\nEnter the student's information:")
    name = input("Full Name: ")
    if name.isdigit():
        print("Invalid name, as it cannot be made out of just nubers")
        add_student(students)
    else:
        section = input("Enter thestudent's class ID (for example 11B): ")
    #for this part....originally I had 1 function per subject, but Alex explained that, since all of them did pretty much the same, it'll be more efficient to just create 1 function that shifted between subject (with a parameter for each subject)
    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social = get_valid_grade("Social Studies")
    science = get_valid_grade("Science")

    average = (spanish + english + social + science) / 4
    student = {"Name": name,"Class ID": section,"Grades": {"Spanish": spanish,"English": english,"Social Studies": social,"Science": science},"Average": average}
    students.append(student)
    print("The information was added correctly, please review it: \n\n", student)

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter {subject} grade (keep in mind that the entered score cannot be greater than 100 or lower than 0): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("The entered score cannot be greater than 100 or lower than 0, try again")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

def view_students(students):
    if len(students)==0:
        print("No information entered yet, try entering data first before trying to review it")
    else:
        for student in students:
            print("Name: ", student['Name'])
            print("Class ID: ",student['Class ID'])
            for subject, grade in student['Grades'].items():
                print(f"{subject}: {grade}")
            print(f"Average: {student['Average']:.2f}")

def top_3_students(students): #I have to be honest, I did get help from a friend of mine to get this one to work.....he tried to explain the Lambda part.....but I didn't get it quite well
    if len(students)<3 :
        print("No information entered yet or at least not enough information yet, try entering data first before trying to get the Top 3 scores")
    else:
        sorted_students = sorted(students, key=lambda x: x["Average"], reverse=True)[:3]
        print("\nTop 3 students by average grade:")
        for i, student in enumerate(sorted_students, start=1):
            print(f"{i}. {student['Name']} - Average: {student['Average']:.2f}")

def average_of_all_students(students):
    if len(students)==0:
        print("No information entered yet, try entering data first before trying to get the global avarage")
    else:
        overall_average = sum(student['Average'] for student in students) / len(students)
        print(f"\nOverall average of all students: {overall_average}")