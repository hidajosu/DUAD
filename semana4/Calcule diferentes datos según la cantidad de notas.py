"""Dada n cantidad de notas de un estudiante, calcular:
1. Cuantas notas tiene aprobadas (mayor a 70).
2. Cuantas notas tiene desaprobadas (menor a 70).
3. El promedio de todas.
4. El promedio de las aprobadas.
5. El promedio de las desaprobadas."""

amount_grades=int(input("Enter the amount of grades you have to evaluate: "))
counter=0
approved_values=0
approved_grades=0
non_approved_values=0
non_approved_grades=0
while(counter<amount_grades):
    grade=int(input("Enter the grade/score: "))
    if(grade>=70):
        approved_grades=counter+1
        approved_values=approved_values+grade
        counter=counter+1
    else:
        non_approved_grades=counter+1
        non_approved_values=non_approved_values+grade
        counter=counter+1
print("The amount of approved grades is: ",approved_grades)
print("The amount of non-approved grades is: ",non_approved_grades)
print("The average score of all the grades is: ", (approved_values+non_approved_values)/amount_grades)
if(approved_grades>0):
    print("The average score of the approved grades is: ", approved_values/approved_grades)
else:
    print("There's no way to tell the average for the approved grades since there are none")
if(non_approved_grades>0):
    print("The average score of the non-approved grades is: ", non_approved_values/non_approved_grades)
else:
    print("There's no way to tell the average for the non-approved grades since there are none")
