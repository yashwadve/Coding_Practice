arr = [10, 25, 5, 40, 30]

largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)