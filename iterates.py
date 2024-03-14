#ask a user to provide five numbers then compute and display the total

total_number = 0

for numbers in range(5):
    user_number = int(input("enter number: "))
    total_number +=user_number
print(f"\ntotal number: {total_number}")