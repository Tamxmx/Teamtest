def calAge(b):
    return 2567 - b

def calRank(b):
    if b == "A":
        return "High Distinction"
    elif b == "B+":
        return "Distinction"
    elif b == "B":
        return "Distinction"
    elif b == "C+":
        return "Good"
    elif b == "C":
        return "Good"
    elif b == "D+":
        return "Normal"
    elif b == "D":
        return "Normal"
    elif b == "F":
        return "Failed"
    else:
        return "Error Rank"
    
def read_from_file(filename="Textfile.text"):
    data = {}

    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split(" : ")
            data[key] = value
    
    return data

file_data = read_from_file("Textfile.text")

print(f"Name: {file_data.get('Name')}")
print(f"Age: {calAge(int(file_data.get('Age')))}")
print(f"Software Testing Grade: {calRank(file_data.get('Software Testing Grade'))}")