gender = input("enter your gender: ")
award = "none"
cgpa = 5.0
cgpa_class = "none"
if cgpa == 5.0: 
    if gender=="male":
        award = "gold medal" 
    elif gender=="female":
        award = "gold medal and a laptop"
else:
    print("wrong gender")
print(f"\nyou have have won {award}\n")


