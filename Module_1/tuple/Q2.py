# Write a program to count the occurrence of an element in a tuple.
t = (1, 2, 3, 2, 4, 2)

count = 0

for i in t:
    if i == 2:
        count = count + 1

print("Occurrence =", count)
