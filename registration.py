# write a program to register users and the password should not exceed 10 characters it should have atleast 6 characters.

user_name = input("enter username: ")
password = input("enter password: ")

if len(password) > 10:
    print("password should not exceed 10 characters")
elif len(password) < 6:
    print("password should be atleast 6 charaters")
else:
    confirm_password = input("confirm password: ")
    if password == confirm_password:
        print("passwrd created successfully")
    else:
        print("password doesnot match, please try again ")