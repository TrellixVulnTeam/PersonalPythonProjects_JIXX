score = int(input("What is your score: "))

if score >= 90:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = "C"
        else:
            if score >= 60:
                grade = "D"
            else:
                grade = "F"

if grade == "A" or grade == "F":
    print("Your grade is an " + grade + ".")
else:
    print("Your grade is a " + grade + ".")
