numbers = [10, 20, 30, 40]
target = 10

index = 0
found = False

for num in numbers:
    if num == target:
        print("Found at index:", index)
        found = True
    index = index + 1

if found == False:
    print("Number not found")