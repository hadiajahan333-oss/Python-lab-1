total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = total / 5

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)