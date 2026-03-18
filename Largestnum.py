numbers = [3, 7, 2, 9, 5]

largest = numbers[0]   # assume first element is largest

for i in range(1, len(numbers)):

    if numbers[i] > largest:
        largest = numbers[i]

print("Largest number:", largest)