def display_menu():
    print("""
          
                            ====================Menu====================
          Enter one of the following options so the system can assist you in an specific way:
          For the system to work, you need to input a number from 0 to 7, any other digit or character will not work
    -->1: This option will allow you to enter new information related to an specific student
    -->2: This option will allow you to view all students' information
    -->3: This option will allow you to view the top 3 students by average grade (as long as there are at least 3 grades stored in the system)
    -->4: This option will allow you to view the overall average of all students
    -->5: This option will allow you to export the entered data to a CSV file
    -->6: This option will allow you to import data from a CSV (that file has to exist first)
    -->7: This option will allow you to exit the system""")

def get_choice_from_user():
    choice = input("Enter an option (you need to input a number from 0 to 7, any other digit or character will not work): ")
    if choice.isdigit():
        choice=int(choice)
        return choice
    else:
        print("No valid input entered, try again")
        get_choice_from_user()
    
    
    
    
    
    
    
    