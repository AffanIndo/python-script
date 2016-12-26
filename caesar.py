#!usr/bin/env python
"""
caesar.py
Encrypt or decrypt text based from caesar cipher
Credit to: I82Much - http://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
"""

def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
    print("Your ciphertext is: ", cipherText)
    return cipherText

if __name__ == '__main__':
    plainText = input("Insert your text:\n")
    shift = int(input("Insert how many shift:"))
    caesar(plainText, shift)
