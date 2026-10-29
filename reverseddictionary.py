data = {'a': 1, 'b': 2, 'c': 3}

reversed_data = {}

for key, value in data.items():
    reversed_data[value] = key

print(reversed_data)