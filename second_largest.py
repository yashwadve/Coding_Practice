# second largest

arr = [10, 20, 5, 40, 30]

largest = arr[0]
second = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second:
        second = arr[i]

print(second)