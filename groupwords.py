words = ['apple', 'ant', 'banana', 'ball', 'cat']

grouped = {}

for word in words:
    first_letter = word[0]

    if first_letter in grouped:
        grouped[first_letter].append(word)
    else:
        grouped[first_letter] = [word]

print(grouped)