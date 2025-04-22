from turtle import st
from menu import display_menu, get_choice_from_user
from actions import add_student, view_students, top_3_students, average_of_all_students
from data import export_data, import_data

students = [] #I still can't get this project to work withou this variable as a Global variable :/

def main(): #I could've done this using the "match-case statement"....you tell e if I need to change it or not
    while True:
        display_menu()
        choice = get_choice_from_user()
        if choice == 1:
            add_student(students)
        elif choice == 2:
            view_students(students)
        elif choice == 3:
            top_3_students(students)
        elif choice == 4:
            average_of_all_students(students)
        elif choice == 5:
            export_data(students)
        elif choice == 6:
            import_data(students)
        elif choice == 7:
            print("You've chosen to exit the program, good bye")
            break
        else:
            print("Invalid option, please try again")

print("""======================================================================================================================================================
Welcome to the 1st project from the Lyfter Academy, this is a Grade Control System which has the intent og helping out managins student grades in an easier way
======================================================================================================================================================""")
main()

    