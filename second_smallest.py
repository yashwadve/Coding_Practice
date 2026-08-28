arr = [10, 20, 5, 40, 30]

smallest = arr[0]
second = arr[0]

for i in range(1, len(arr)):
    if arr[i] < smallest:
        second = smallest
        smallest = arr[i]
    elif arr[i] < second:
        second = arr[i]

print(second)