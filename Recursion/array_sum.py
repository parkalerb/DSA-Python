def array_sum(arr, index):
    if index == len(arr):
        return 0

    return arr[index] + array_sum(arr, index + 1)


numbers = [10, 20, 30, 40, 50]

result = array_sum(numbers, 0)

print("Sum of array is:", result)