#!/usr/bin/python3
import string
for letter in string.ascii_lowercase:
    if letter not in 'qe':
        print(letter, end ="")
