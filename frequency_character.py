string = "hello"

frequency = {}

for i in range(len(string)):
    ch = string[i]

    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, "→", frequency[ch])