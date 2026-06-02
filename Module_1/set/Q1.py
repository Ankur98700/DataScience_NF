# Given two sets, check if one set is a subset of another.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

flag = True

for i in set1:
    if i not in set2:
        flag = False

if flag:
    print("Subset")
else:
    print("Not a Subset")
