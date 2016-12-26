#!usr/bin/env python
"""
euler-even-fibonacci-numbers.py
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

fibList = []

a, b = 0, 1
while a < 4000000:
    a, b = b, a+b
    if a <= 4000000:
        fibList.append(a)

total = 0
for i in fibList:
    if i % 2 ==0:
        total +=i

print(total)
