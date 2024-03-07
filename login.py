'''secrete_username = "admin"
secrete_password = "user 1234"

login_attempts = 0
while login_attempts <3:

    username = input("enter user name: ")
    password = input("enter password: ")

    login_attempts +=1'''

secrete_username = "admin"
secrete_password = "user 1234"

login_attempts = 0
while login_attempts <3:
    username = input("enter username: ")
    password = input("enter password: ")

    if username == secrete_username and password == secrete_password:
        print("\tWelcome to IUIU ERP")
        break
    else:
        print("Invalid username and password")
    login_attempts += 1