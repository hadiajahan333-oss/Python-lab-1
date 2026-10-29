numbers = [2, 3, 2, 5, 3, 2, 5, 8]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)