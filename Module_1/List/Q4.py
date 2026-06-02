# Write a program to count even and odd numbers in a list.
numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)
