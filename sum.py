numbers = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nSum:", total)
print("Average:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)