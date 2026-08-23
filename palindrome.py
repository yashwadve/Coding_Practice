# check string is palindrome

string  = "madam"

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    
# check number is palindrome

num = 121
original = num
reverse = 0

while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10
    
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")