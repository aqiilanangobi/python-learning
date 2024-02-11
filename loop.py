subject_scores = []
subject_names = []

for i in range(4):
     subject_name = input("enter subject name: ") 
     subject_names.append(subject_name)

for i in range(4):
     subject_score = int(input(f"enter subject score: "))
     subject_scores.append(subject_score)
     print(subject_score)

for i in range(4):
     print(f"{subject_names[i]}:{subject_scores[i]}")

total_score = subject_scores[0] + subject_scores[1] + subject_scores[2] + subject_scores[3]
print(f"total score: {total_score}")

average_score = total_score/4
print(f"average_score: {average_score}")