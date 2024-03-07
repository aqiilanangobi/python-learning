full_name =  input("enter your name: ")
english_score  = int(input("enter english score: "))
maths_score  = int(input("enter maths score: "))
science_score  = int(input("enter science score: "))
arts_score  = int(input("enter arts score: "))
total_mark  = english_score + maths_score + science_score + arts_score
average_score = total_mark/4
print(total_mark)
print(average_score)