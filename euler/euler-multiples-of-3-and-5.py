#!usr/bin/env python
"""
euler-multiples-of-3-and-5.py
Find the sum of all the multiples of 3 or 5 below 1000.
"""

number = []

for i in range(1,1001):
    if i % 15 == 0:
        number.append(i)
    elif i % 3 == 0:
        number.append(i)
    elif i % 5 == 0:
        number.append(i)
    else:
        pass

total = 0
for item in number:
    total += item

print(total)
