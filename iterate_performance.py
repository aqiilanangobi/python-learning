students = ["Aqiila","shan","raha","eunice"]

pass_count = 0
fail_count =0

number_of_subjects = int(input("enter subject number: "))
average_pass_mark = float(input("Enter average pass mark: "))

for student in students:
    student_total = int(input(f"{student}'s total: "))
    student_average = float(student_total/number_of_subjects)

    if student_average >= 50:
        pass_count += 1
    else:
        fail_count += 1

print(f"\nTotal pass: {pass_count}\nTotal failures: {fail_count}")    

