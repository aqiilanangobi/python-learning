students = ["Aqiila","shan","raha","eunice"]
subjects = ["maths","science","english","SST"]

pass_count = 0
fail_count =0

number_of_subjects = int(input("enter subject number: "))
average_pass_mark = float(input("Enter average pass mark: "))

for student in students:
    print(f"\n\tEnter {student}'s Scores")
    student_total = 0

    for subject in subjects:
        subject_score = int(input(f"{subject}: "))
        student_total += subject_score

student_average = student_total/number_of_subjects

if student_average >= average_pass_mark:
    pass_count += 1
else:
    fail_count += 1

print(f"\nTotal pass: {pass_count}\nTotal failures: {fail_count}") 