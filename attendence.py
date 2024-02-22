number_of_classes = 15
medical_cause = " "


classes_attended = int(input("enter number of classes: "))
percentage_of_classes_attended = int((classes_attended/15)*100)

print(f"classes attended: {classes_attended}\tpercentage of classes attended: {percentage_of_classes_attended}")

if percentage_of_classes_attended < 75:
    if  medical_cause:
        medical_cause = input("enter 'Y' or 'N': ")
        print(f"medical_cause: {medical_cause} ")
        if 'Y':
            print("student allowed to sit for the exam")
        else:
            print("not allowed to sit for the exams")

else:
    print("allowed to sit for the exams")

