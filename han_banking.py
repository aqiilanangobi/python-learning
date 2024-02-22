current_balance=1000000
one_time_password="5678"
password="1234"
print("welcome to han banking online services ")
user_name=input("enter the account user name ")
acc_no=input("enter the account number ")
password=input("enter the password ")
if password==one_time_password:
    print("welcome to your account ")
else:
    print("wrong password encountered ")
option_1="1"
option_2="2"
option_3="3"
print(f"{option_1} depoist\n{option_2} withdraw\n{option_3} check balance")
user_input=input("\nenter option: ")
if user_input==option_1:
    depoist_money=int(input("enter depoist money" ))
    if depoist_money>2000:
        balance =current_balance + depoist_money
        password=input("enter the one_time_password ")
        if one_time_password==one_time_password:
            print("login successful")
        else:
            print("invalid password")
        print(f"dear beloved customer you have depoisted {balance} thank you for banking with us\n")
elif user_input==option_2:
    amount_withdrawn=int(input("enter the amount you wish to withdraw "))
    if current_balance>amount_withdrawn:
        balance=current_balance-amount_withdrawn
        password=input("enter the OTP ")
        print(f"dear beloved customer you have withdrawn {amount_withdrawn}\n")
elif user_input==option_3:
    print(f"dear customer your account balance is {current_balance}")
else:
    print("please contact the nearest agent for further help\nTHANK YOU\n\nmanagement")


    