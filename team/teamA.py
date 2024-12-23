def calAge(a):
    return 2024 - a 

def calGrade(a):
    if 100 >= a >= 80:
        return "A"
    elif 80 > a >= 75:
        return "B+"
    elif 75 > a >= 70:
        return "B"
    elif 70 > a >= 65:
        return "C+"
    elif 65 > a >= 60:
        return "C"
    elif 60 > a >= 55:
        return "D+"
    elif 55 > a >= 50:
        return "D"
    elif 50 > a >= 0:
        return "F"
    else:
        return "Error Score"
    
Name = input("Name : ")
Era = int(input("Christian Era : "))
Score = int(input("Software Testing Score : "))

age = calAge(Era)
grade = calGrade(Score)

print(f"Name : {Name}")
print(f"Age : {age}")
print(f"Software Testing Grade : {grade}")

with open("Textfile.text", "w") as file:
    file.write(f"Name : {Name}\n")
    file.write(f"Age : {age}\n")
    file.write(f"Software Testing Grade : {grade}\n")