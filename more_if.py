# mulitiple if is used if we have morethan two alternatives and it requires you to use multiple ifs.
birth_year = int(input("enter your birth_year: "))
current_year = 2021
age = current_year - birth_year
print(f"your age: {age}\n ")
if age <=3:
    print("this is a baby")
elif age<=10:
    print("this ia a kid")
elif age<=20:
    print("this is a teenager\n")
elif age<=35:
    print("this is a youth")
elif age<=50:
     print("this is an adult")
elif age>50:
    print("tis is an elder")

else:
    print("no category for you")


