stud_name = input("Enter your name; ")
age = int(input("Enter your age; "))

print(stud_name)
print(age)

def age_calcular():

    if age >= 18:
        print(True)
    else:
        print(False)

age_calcular()