user = int(input("Enter the number of terms in the Palindrome series: "))
sec = user
count = 0
print("Palindrome series up to", user, "terms:")

while 0 < sec:
    num = sec % 10
    count = count *10 +num
    sec = sec // 10

if user == count:
    print("The number is a palindrome.")    
else:
    print("The number is not a palindrome.")