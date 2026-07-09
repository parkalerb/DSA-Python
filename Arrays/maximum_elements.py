# Maximum Element in an Array

numbers = [12, 45, 7, 89, 34, 56]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Array :", numbers)
print("Maximum Element :", maximum)