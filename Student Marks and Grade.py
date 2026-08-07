# Student Marks and Grade Program

print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0

for i in range(1, n + 1):
    mark = int(input("Enter mark for subject " + str(i) + ": "))
    total += mark

average = total / n

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if average >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("\nThank you!")