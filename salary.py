
RATE_0F_PAY = 35000
employee_name = input("\nenter employee_name: ")
hours_worked = int(input("enter hours_worked: "))

wage = hours_worked*RATE_0F_PAY
print(f"your salary is {wage}")

if wage >500000:
    print("\nyou are required to pay tax\n")
else:
    print("\nNo tax to be paid\n")


