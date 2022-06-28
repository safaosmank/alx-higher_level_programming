#!/usr/bin/python3
for num in range(100):
    if num != 99:
        print(f"{num}, ")
    else:
        print(f"{num}")
        print("{},".format(num), end = " ")
    else:
        print("{}".format(num))
