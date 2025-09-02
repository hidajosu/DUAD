def bubble_sort(random_numbers):
    for i in range(0, len(random_numbers)):
        for j in range(0, len(random_numbers) - i - 1):
            if random_numbers[j] > random_numbers[j + 1]:
                # Swap
                temp = random_numbers[j]
                random_numbers[j] = random_numbers[j + 1]
                random_numbers[j + 1] = temp

# Example usage:
numbers = [5, 2, 8, 1, 9]
print("Before bubble sort:", numbers)
bubble_sort(numbers)
print("After bubble sort:", numbers)