def calculate_sum(*args):
    total = 0

    for num in args:
        total = total + num

    return total

print("Sum:", calculate_sum(10, 20, 30, 40))