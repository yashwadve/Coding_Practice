string = "hello"

vowels = 0
consonants = 0

for i in range(len(string)):
    ch = string[i]

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        vowels = vowels + 1
    elif ch >= 'a' and ch <= 'z':
        consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)