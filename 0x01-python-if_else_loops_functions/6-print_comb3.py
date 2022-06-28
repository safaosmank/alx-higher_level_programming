#!/usr/bin/python3
for f_num in range(10):
    for l_num in range(f_num + 1, 10):
        if not (f_num == 8 and l_num == 9):
            print("{}{},".format(f_num, l_num), end=" ")
        else:
            print("{}{}".format(f_num, l_num))
