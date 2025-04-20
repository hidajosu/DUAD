import csv

def export_data(students):
    if not students:
        print("There's no data to export, please enter information first and then try exporting it.")
        return
    with open("students.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Class ID", "Spanish", "English", "Social Studies", "Science", "Average"])
        for index in students:
            writer.writerow([
                index["name"],
                index["class ID"],
                index["grades"]["Spanish"],
                index["grades"]["English"],
                index["grades"]["Social Studies"],
                index["grades"]["Science"],
                index["average"]
            ])
    print(f"Data exported successfully to {"students.csv"}.")

def import_data(students):
    try:
        with open("students.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name, section, spanish, english, social, science, average = row
                student = {
                    "name": name,
                    "section": section,
                    "grades": {
                        "spanish": spanish,
                        "english": english,
                        "social Studies": social,
                        "science": science
                    },
                    "average": average
                }
                students.append(student)
        print(f"Data imported successfully from {"students.csv"}.")
    except Exception as error:
        print(f"There seems to be an error: {error}")