str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagram")
else:
    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        print("Anagram")
    else:
        print("Not Anagram")