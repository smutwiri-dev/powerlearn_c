# Empty list
my_list = []

#add values to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert 15 at the second position
my_list.insert(1, 15)

# Extend list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort my_list in ascending order.
my_list.sort()

# print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("The index of 30 is:", index_30)

# Final list
print("Final list:", my_list)