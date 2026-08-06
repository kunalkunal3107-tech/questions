# 6. Create a dynamic list, display the list and perform any task
# * Update element
# * Insert new element
# * Insert new list
# * Delete any element 
# * Sum of a list
# * Find the smallest element 
# * Find the largest element


print("Enter the number of elements in the list:")
n = int(input("Enter here: "))
number = []
for i in range(n):
    element = int(input(f"Enter the {i+1} element : "))
    number.append(element)

while True:


    print("1).The list is:", number)
    print("2).Update element")
    print("3).Insert new element")
    print("4).Insert new list")
    print("5).Delete any element")
    print("6).Sum of a list")
    print("7).Find the smallest element")
    print("8).Find the largest element")
    
    user = int(input("Enter your choice: "))




    if user == 1:
        print("The list is:", number)

    elif user == 2:
        index = int(input("Enter the index of the element to update: "))
        new_value = int(input("Enter the new value: "))
        number[index] = new_value
        print("Updated list:", number)

    elif user == 3:
        new_element = int(input("Enter the new element to insert in list:"))
        number.append(new_element)
        print("Insert Updated in list:", number)

    elif user == 4:
        new_list = []
        m = int(input("Enter the number of element in new list :"))
        for i in range(m):
            new_element = int(input(f"Enter the {i+1} element :"))
            new_list.append(new_element)
        number.extend(new_list)
        print("Updated list after inserting new list:", number)

    elif user == 5:
        index = int(input("Enter the index of the element to delete: "))
        if 0 <= index < len(number):
            del number[index]
            print("Updated list after deletion:", number)
        else:
            print("Invalid index!")

    elif user == 6:
        total_sum = sum(number)
        print("Sum of the list:", total_sum)

    elif user == 7:
        smallest_element = min(number)
        print("Smallest element in the list:", smallest_element)

    elif user == 8: 
        largest_element = max(number)
        print("Largest element in the list:", largest_element)
