nums = [2, 7, 11, 15]
target = 9

seen = {}

for num in nums:
    required = target - num

    if required in seen:
        print(required, "+", num, "=", target)
        break

    seen[num] = 1
    