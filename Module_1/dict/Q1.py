# Write a program to create a dictionary from two lists: one of keys and one of values.
keys = ["name", "age", "city"]
values = ["Ankur", 21, "Noida"]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)
