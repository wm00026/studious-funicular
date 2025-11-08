"""
A basic palindrome checker

Author: @wm00026
"""

def palindrome_check(word):
    
    if word == word[::-1]:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

runs = input("Enter a number: ")

loops = int(runs)

for _ in range(loops):
    word = input("Enter a word: ")
    palindrome_check(word)