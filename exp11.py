import random
numbers = [random.randint(1, 100) for _ in range(20)]
print("List of random numbers:")
print(numbers)
average = sum(numbers) / len(numbers)
print("Average of elements:", average)
print("Largest value:", max(numbers))
print("Smallest value:", min(numbers))
unique_numbers = list(set(numbers))  # remove duplicates
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second smallest value:", unique_numbers[1])
    print("Second largest value:", unique_numbers[-2])
else:
    print("Not enough unique elements to find second largest/smallest")
even_count = sum(1 for num in numbers if num % 2 == 0)
print("Number of even numbers:", even_count)
