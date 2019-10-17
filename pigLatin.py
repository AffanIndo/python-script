#!usr/bin/env python
"""
pigLatin.py
Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules
"""

print("Pig Latin translator. Insert the text you want to translate into Pig Latin. To quit, type 'quit'")
while True:
    word = input("Insert text: ")
    if word == "":
        print("the text is empty")
    elif word == "quit":
        exit()
    else:
        print(word[1:]+"-"+word[0]+"ay")
