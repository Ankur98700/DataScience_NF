# Write a program to sort a dictionary by its values.
d = {"a": 5, "b": 2, "c": 8, "d": 1}

for value in sorted(d.values()):
    for key in d:
        if d[key] == value:
            print(key, ":", value)
