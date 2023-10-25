#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:03:02 2023

@author: manelson
"""

# Exercise 1:
# Return True if input is the number 2 or string 2
def is_two(x):
    if x in [2,'2']:
        return True
    else:
        return False

assert is_two(2) == True
assert is_two('2') == True
assert is_two(4) == False
assert is_two('aeiou') == False
print("Exercise 1 is correct")


# Exercise 2
# Return true if the passed string is a vowel and false otherwise
def is_vowel(x):
    vowels = ['a','e','i','o','u']
    
    # Check if string has numbers
    if x.isalpha():
        if x.lower() in vowels:
            return True
    
    # Return false if nothing else
    return False

assert is_vowel('a') == True
assert is_vowel('c') == False
assert is_vowel('A') == True
assert is_vowel('H') == False
print("Exercise 2 is correct")

# Exercise 3
# Return True if the string is a consonant, False otherwise
# Use the is_vowel function to accomplish this
def is_consonant(x):
    
    if x.isalpha():
        return not is_vowel(x)
    
    # Return false if nothing else
    return False

assert is_consonant('a') == False
assert is_consonant('B') == True
assert is_consonant('8') == False
assert is_consonant('i') == False
assert is_consonant('Y') == True
print('Exercise 3 is correct')

# Exercise 4
# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the word
# starts with a consonant.
def the_titler(x):
    if is_consonant(x[0]):
        return x.title()
    else:
        return x.lower()
    
assert the_titler('the') == 'The'
assert the_titler('word') == 'Word'
assert the_titler('android') == 'android'
assert the_titler('forewarned') == 'Forewarned'
assert the_titler('cUpCaKeS') == 'Cupcakes'
print("Exercise 4 is correct")

# Exercise 5
# Exercise 6
# Exercise 7
# Exercise 8
# Exercise 9
# Exercise 10
# Exercise 11


### Additional Exercise

# - Once you've completed the above exercises, 
# follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.
