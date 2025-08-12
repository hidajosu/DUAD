def bubble_sort_right_to_left(random_numbers):
    for i in range(0, len(random_numbers)):
        for j in range(len(random_numbers) - 1, i, -1):
            if random_numbers[j] < random_numbers[j - 1]:
                # Swap
                temp = random_numbers[j]
                random_numbers[j] = random_numbers[j - 1]
                random_numbers[j - 1] = temp

numbers = [5, 2, 8, 1, 9]
print("Before bubble sort:", numbers)
bubble_sort_right_to_left(numbers)
print("After bubble sort:", numbers)