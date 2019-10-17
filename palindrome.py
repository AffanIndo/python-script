#!usr/bin/env python
"""
palindrome.py
Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
"""

string = input("Insert a string: ")
if string[::-1] == string:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")
