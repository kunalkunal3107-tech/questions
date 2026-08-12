# 6. Create a dynamic list, display the list and perform any task
# * Update element
# * Insert new element
# * Insert new list
# * Delete any element 
# * Sum of a list
# * Find the smallest element 
# * Find the largest element

# user = int(input("How many elements do you want to enter? "))
# my_list = []
# for i in range(user):
#     element = int(input(f"Enter your {i+1} element:"))
#     my_list.append(element)

# print("Your list is:", my_list)

# while True:
     
#     print("1).The list is:", my_list)
#     print("2).Update element")
#     print("3).Insert new element")
#     print("4).Insert new list")
#     print("5).Delete any element")
#     print("6).Sum of a list")
#     print("7).Find the smallest element")
#     print("8).Find the largest element")

#     choice = int(input("Enter your choice: "))

#     if choice ==1:
#         print("The list is :", my_list)

#     elif choice == 2:
#         index = int(input("Enter the index of the element to update:"))
#         new = int(input("Enter the new value:"))
#         my_list[index] = new
#         print("Update list is:", my_list)

#     elif choice == 3:
#         new_element = int(input("Enter the new element to insert in list: "))
#         my_list.append(new_element)
#         print("Updated list is:", my_list)

#     elif choice == 4:
#         new_list = []
#         m = int(input("Enter the number"))
#         for i in range(m):
#             new_element = int(input(f"Enter the {i+1} element: "))
#             new_list.append(new_element)
#             new_list.extend(my_list)
#             print("Updated list after inserting new list is:", new_list)

#     elif choice == 5:
#         index = int(input("Enter the index of the element to delete: "))
#         if 0 >= index > len(my_list):
#             print("Invalid index. Please try again.")
#         else:
#             del my_list[index]
#             print("Updated list after deleting element is:", my_list)

#     elif choice == 6:
#         summ = sum(my_list)
#         print("The sum of the list is:",summ)

#     elif choice == 7:
#         minn = min(my_list)
#         print("The smallest element in the list is:",minn)

#     elif choice == 8:
#         maxx = max(my_list)
#         print("The largest element in the list is:",maxx)




class dynamic_list:
    def __init__(self):
        self.my_list = []
        user = int(input("How many elements do you want to enter? "))
        for i in range(user):
            element = int(input(f"Enter your {i+1} element:"))
            self.my_list.append(element)

    def show_list(self):
        print("The list is:", self.my_list)

    def update_element(self):
        index = int(input("Enter the index of the element to update:"))
        new = int(input("Enter the new value:"))
        self.my_list[index] = new
        print("Updated list is:", self.my_list)

    def insert_new_element(self):
        new_element = int(input("Enter the new element to insert in list: "))
        self.my_list.append(new_element)
        print("Updated list is:", self.my_list)


aa = dynamic_list()

print("1).The list is:")
print("2).Update element")
print("3).Insert new element")
print("4).Insert new list")
print("5).Delete any element")
print("6).Sum of a list")
print("7).Find the smallest element")
print("8).Find the largest element")

choic = int(input("Enter your choice: "))

if choic == 1:
    aa.show_list()