import csv

def export():
    global headers
    headers=("Name", "Student's Class ID", "Spanish", "English grade", "Social Studies grade", "Science grade", "Avarage score for this student's grades")
    with open("Score file.csv", "w", encoding="utf-8") as file:
        writer=csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(globalList)