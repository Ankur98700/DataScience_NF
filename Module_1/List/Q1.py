# Write a program to find the largest and smallest elements in a list.
numbers = [10, 5, 25, 8, 30]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)
