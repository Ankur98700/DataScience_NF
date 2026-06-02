# Write a program to reverse a list without using built-in reverse functions.

lst = [10, 20, 30, 40, 50]

rev = []

i = len(lst) - 1

while i >= 0:
    rev.append(lst[i])
    i = i - 1

print("Original List:", lst)
print("Reversed List:", rev)
