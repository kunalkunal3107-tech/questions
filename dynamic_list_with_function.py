# 6. Create a dynamic list, display the list and perform any task
# * Update element
# * Insert new element
# * Insert new list
# * Delete any element 
# * Sum of a list
# * Find the smallest element 
# * Find the largest element
class dynamic_list:

    def __init__(self):
        self.n = int(input("Enter the number of elements in the list which you want to see in your list: "))
        self.number = []
        for i in range(self.n):
            element = int(input(f"Enter the {i+1} element : "))
            self.number.append(element)

    def show_list(self):
        print("The list is:", self.number)

    def update_element(self):
        index = int(input("Enter the index of the element you want to update (0-based indes):"))
        if index < 0 or index >= len(self.number):
            print("Invalid index. Please try again.")
            return
        else:
            new_value = int(input("Enter the element which you want to update:"))
            self.number[index] = new_value
            print("The updated list is:", self.number)

    def insert_element(self):
        new_element = int(input("Enter the new element which you want to insert:"))
        self.number.append(new_element)
        print("The updated list is:", self.number)

    def insert_list(self):
        new_list = []
        n = int(input("Enter the number of elements in the new list: "))
        for i in range(n):
            element = int(input(f"Enter the {i+1} element of the new list:"))
            new_list.append(element)
        self.number.extend(new_list)

    def delete_element(self):
        index = int(input("Enter the index of the element you want to delete (0-based index):"))
        if index < 0 or index >= len(self.number):
            print("Invalid index. Please try again.")
            return
        else:
            deleted_element = self.number.pop(index)
            
            print(f"The element {deleted_element} has been deleted.")
            print("The updated list is:", self.number)

    def sum_list(self):
        summ = sum(self.number)
        print("The sum of the list is:", summ)

    def find_smallest(self):
        if not self.number:
            print("The list is empty.")
            return
        smallest = min(self.number)
        print("The smallest element in the list is:", smallest)

    def find_largest(self):
        if not self.number:
            print("The list is empty.")
            return
        largest = max(self.number)
        print("The largest element in the list is:", largest)




user = dynamic_list()



print("1).The list is:")
print("2).Update element")
print("3).Insert new element")
print("4).Insert new list")
print("5).Delete any element")
print("6).Sum of a list")
print("7).Find the smallest element")
print("8).Find the largest element")

choice = int(input("Enter your choice: "))

if choice == 1:
    user.show_list()

if choice == 2:
    user.update_element()

if choice == 3:
    user.insert_element()

if choice == 4:
    user.insert_list()

if choice == 5:
    user.delete_element()

if choice == 6:
    user.sum_list()

if choice == 7:
    user.find_smallest()

if choice == 8:
    user.find_largest()