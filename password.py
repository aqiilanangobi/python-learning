#checking whether user has entered the correct password.

saved_password = "user @123"
user_name = input("enter user name: ")
password = input("enter password: ")
if password == saved_password:
    print("Login successfull")
else:
    print("invalid password")