arr = [1, 2, 2, 3, 4, 4]
result = list(set(arr))
print(result)


# wihtout set
arr = [1, 2, 2, 3, 4, 4]

result = []

for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])

print(result)