# program to determine class of students using CPGA
cgpa = float(input("enter CGPA: "))
cgpa_class = "none"
award = "none"
gender = input("enter your gender: ")
if cgpa<=1.9:
    cgpa_class= "fail"
elif cgpa<=2.4:
    cgpa_class= "pass"
elif cgpa<=3.5:
    cgpa_class= "second class lower"
elif cgpa<= 4.4:
    cgpa_class= "second class upper"
elif cgpa<=5.0:
    cgpa_class= "first class"
    if gender== "male":
        award = "Gold medal"
    elif gender== "female":
        award = "Gold medal and a laptop"
    else:
        print("wrong gender")
    print(f"\nyou have won {award}\n")
else:
    print("not a valid CGPA")


print(f"\nCPGA: {cgpa}\tclass: {cgpa_class}\n")