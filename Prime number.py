user = int(input("Enter your number of series"))

if user <=1:
    print("It's a not prime number")
else:
    for i in range(2,user):
        if user % i ==0:
            print("It's not a prime number")
            break
        else:
            print("It's a prime number")
            break