#!/usr/bin/python3
for char in reversed(range(97, 123)):
    print("{}".format(chr(char) if (char % 2 == 0) else chr(char - 32)), end="")
