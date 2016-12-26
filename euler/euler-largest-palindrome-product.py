#!usr/bin/env python
"""
euler-largest-palindrome-product.py
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = []
for x in range(100, 1000):
    for y in range(100, 1000):
        allSum = x*y
        if str(allSum) == str(allSum)[::-1]:
            palindrome.append(allSum)
print(palindrome[len(palindrome)-1])
