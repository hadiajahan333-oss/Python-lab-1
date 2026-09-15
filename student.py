name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

# Check if any subject is below 40
if any(mark < 40 for mark in marks):
    result = "Fail"
else:
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

print("\n----- STUDENT MARKSHEET -----")
print("Name:", name)
print("Roll No:", roll_no)

for i in range(5):
    print(f"Subject {i + 1} Marks:", marks[i])

print("Total Marks:", total)
print("Percentage:", percentage, "%")

if any(mark < 40 for mark in marks):
    print("Grade: F")
else:
    print("Grade:", grade)

print("Result:", result)