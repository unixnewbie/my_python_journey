#!/usr/bin/python
myword = raw_input("Enter a word:" )
vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "U"]
if myword[0] in vowels:
   print """The word """ + (myword) + """ start with a vowel"""
else:
   print """The word """ + (myword) + """ doesn't start with a vowel"""
