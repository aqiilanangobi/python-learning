NUMBER_OF_TESTS = 3
count = 1
target = 5

while count <=5:
    student_name = input("enter student name: ")
    test_1 = int(input("enter test 1 score: "))
    test_2 = int(input("enter test 2 score: "))
    test_3 = int(input("enter test 3 score: "))

    total_score = test_1 + test_2 + test_3

    average_score = int(total_score/3)
    print(f"student's name: {student_name}\ntotal score: {total_score}\taverage score: {average_score}")

    count += 1
 