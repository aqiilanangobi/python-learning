pupil_name = input("enter pupil_name: ")
course_work_mark = int(input("enter course work mark: "))
exam_score = int(input("enter exam score: "))
exam_score_out_of_70 = (exam_score/100) * 70
final_score = exam_score_out_of_70 + course_work_mark
print(f"the exam score out of 70 is {exam_score_out_of_70}% and the final score is {final_score}%")

