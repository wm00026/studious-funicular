# Working with Lists in Python

# A basic list with some initial values
list = [1,2,3,4,5]

# Appending an element to the end of the list
list.append(6)
print(list) 

# Removing the last three elements of the list, appending 10 at the end.
list.pop()
list.pop()
list.pop()
list.append(10)
print(list)

# Inserting 0 at the beginning of the list
list.insert(0, 0)
print(list)

# List is cleared
list.clear()

# New list, unsorted.
list = [8,3,19,2,4,5]
print(list)
length = len(list)

# Sorting the list using bubble sort algorithm, O(n^2) time complexity
for i in range(length):
    for j in range(i + 1, length):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
    
print(list)