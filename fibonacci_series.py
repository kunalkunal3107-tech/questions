user = int(input("Enter the number of terms in the Fibonacci series: "))

n1, n2 = 0, 1
count = 0
print("Fibonacci series up to", user, "terms:")

if user <= 0:
   print("Please enter a positive integer.")
else:
   print("Fibonacci sequence:")
   while count < user:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1