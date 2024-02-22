print("\t\tEMPLOYEE SALARY\t") 
employee_name = ""
overtime_hours = 0
overtime_salary = 0
print("""1.pay code 1
      2.pay code 2
      3.pay code 3
      4.pay code 4""")  
pay_code=int(input("enter pay code: "))
if pay_code == 1:
    employee_name = "manager"
    employee_salary = 1500
    print (f"manager salary = {employee_salary}")
elif pay_code == 2:
    employee_name = "hourly worker"
    hours_worked = int(input("enter hours worked: "))
    if hours_worked <= 40:
        employee_salary = 300*hours_worked
    else : 
        overtime_hours = hours_worked - 40
        overtime_salary = int(1.5*overtime_hours*300)
        employee_salary = int(overtime_salary + 300)
    print(f"hourly worker salary: {employee_salary}\t overtime hours: {overtime_hours}\t overtime_salary: {overtime_salary}")
elif pay_code == 3:
    employee_name = "commission worker"
    gross_weekly_sales = int(input("enter gross weekly sales: "))
    employee_salary = int(250 + (0.57 * gross_weekly_sales))
    print(f"commission worker: {employee_salary}")
elif pay_code == 4:
    employee_name = "piece rate worker"
    pieces = int(input("enter number of pieces: "))
    employee_salary = int(200*pieces)
    print(f"piece rate worker salary: {employee_salary}")
else:
    print("invalid pay code")


        