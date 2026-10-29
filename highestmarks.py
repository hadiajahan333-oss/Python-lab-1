marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}

highest = max(marks.values())

for student, mark in marks.items():
    if mark == highest:
        print(student, mark)