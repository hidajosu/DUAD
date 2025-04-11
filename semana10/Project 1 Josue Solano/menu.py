from actions import *
from data import *
from menu import *



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
                    number_students()
                    data_introduction()
                    menu()
                case 2:
                    print("The entered data is: ", globalList)
                    menu()
                case 3:
                    print("As per the chosen option, you wish to see the top 3 avarage scores from the analized students, these avarage scores are: ",top3[0],top3[1],top3[2])
                    menu()
                case 4:
                    print("As per your chosen option, you wish to see the average of the avarage grades from all the students\nThis value is: ",global_avarage)
                    menu()
                case 5:
                    print("As per your chosen option, you wish to export the information into an CSV file")
                    export()
    except Exception as error:
        print("There was an error: ",error)
        menu()           