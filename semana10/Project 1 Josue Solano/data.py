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
                index["Name"],
                index["Class ID"],
                index["Grades"]["Spanish"],
                index["Grades"]["English"],
                index["Grades"]["Social Studies"],
                index["Grades"]["Science"],
                index["Average"]
            ])
    print(f"Data exported successfully to {"students.csv"}.")

def import_data(students):
    try:
        with open("students.csv", mode="r") as file:
            reader = csv.DictReader(file) 
            for row in reader:
                students.append({
                    "Name": row["Name"],
                    "Class ID": row["Class ID"],
                    "Grades": {
                        "Spanish": float(row["Spanish"]),
                        "English": float(row["English"]),
                        "Social Studies": float(row["Social Studies"]),
                        "Science": float(row["Science"])
                    },
                        "Average": float(row["Average"])
                    })
        print(f"Data imported successfully from {"students.csv"}.")
    except Exception as error:
        print(f"There seems to be an error: {error}")