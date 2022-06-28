#!/usr/bin/python3
def uppercase(str):
    for char in range(len(str)):
        letter_code = ord(str[char])
        if letter_code >= 97 and letter_code <= 122:
            letter_code = letter_code - 32
        print("{}".format(chr(letter_code)), end="")
    print()
