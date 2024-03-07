number_of_classes = 15
classes_attended = int(input("enter number of classes: "))
percentage_of_classes_attended = int((classes_attended/15)*100)

print(f"classes attended: {classes_attended}\tpercentage of classes attended: {percentage_of_classes_attended}%")

if percentage_of_classes_attended > 75:
    print(f"{percentage_of_classes_attended}% therefore allowed to sit exams")

else:
    has_medical_cause = input("Do you have any medical cause? 'y'or 'n':  ")
    if has_medical_cause == 'y':
        print(f"{percentage_of_classes_attended}% is below but allowed to sit for exams")
    else:
        print(f"{percentage_of_classes_attended}% not allowed to sit ")



