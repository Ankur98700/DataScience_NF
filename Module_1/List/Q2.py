# Write a program to remove duplicate elements from a list.
numbers = [1, 2, 2, 3, 4, 4, 5]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:")
print(new_list)
