# Write a program to check whether two lists have at least one common element using sets.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]

set1 = set(list1)
set2 = set(list2)

found = False

for i in set1:
    if i in set2:
        found = True
        break

if found:
    print("Common element found")
else:
    print("No common element found")
