
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))



total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average_marks = total_marks / 5



if average_marks >= 90:
    grade = "A++"
elif average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B+"
elif average_marks >= 50:
    grade = "B"
elif average_marks >= 40:
    grade = "C"
else:
    grade = "F"



print("Your grade is:", grade)