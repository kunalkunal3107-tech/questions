user = int(input("Enter a number: "))

# This code for this parten
'''
******
*****
****
***
**
*
**
***
****
*****
'''
# for i in range(user,0,-1):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# for i in range(user):
#     for j in range(i+1):
#         print("*", end="")
#     print()


#==================================================

# This code for this parten 
'''
*****
 ****
  ***
   **
    *
     
    *
   **
  ***
 ****
*****
'''

# for i in range(user,0,-1):
#     for j in range(user-i):
#         print(" ",end="")
        
#     for j in range(i):
        
#         print("*",end="")
#     print()

# for i in range(user+1):
#     for j in range(user-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

# =====================================================
for i in range(user,0,-1):
    for j in range(user-i):
        print(" ",end="")
        
    for j in range(2*i-1):
        
        print("*",end="")
    print()

for i in range(user+1):
    for j in range(user-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

