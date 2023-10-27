#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:03:02 2023

@author: manelson
"""
#%%
# Exercise 1:
# Return True if input is the number 2 or string 2
def is_two(x):
    """

    Parameters
    ----------
    x : string or int
        Takes any argument.

    Returns
    -------
    bool
        Returns True if x is either 2 or '2', False otherwise.

    """
    if x in [2,'2']:
        return True
    else:
        return False

assert is_two(2) == True
assert is_two('2') == True
assert is_two(4) == False
assert is_two('aeiou') == False
print("Exercise 1 is correct")


#%%
# Exercise 2
# Return true if the passed string is a vowel and false otherwise
def is_vowel(x):
    """
    Return if the value passed is a vowel or not.

    Parameters
    ----------
    x : string
        Takes a single-letter string argument.

    Returns
    -------
    bool
        Returns True if the character is a vowel, and False otherwise.

    """
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
assert is_vowel('assert') == False
print("Exercise 2 is correct")

#%%
# Exercise 3
# Return True if the string is a consonant, False otherwise
# Use the is_vowel function to accomplish this
def is_consonant(x):
    """
    Return if the value passed is a consonant or not.

    Parameters
    ----------
    x : string
        Takes a single-letter string argument.

    Returns
    -------
    bool
        Inverses the is_vowel return Returns True if not a vowel, and false otherwise.

    """
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

#%%
# Exercise 4
# Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the word
# starts with a consonant.
def the_titler(x):
    """
    Returns a word with the first letter capitalized if the word starts with a consonant.

    Parameters
    ----------
    x : string
        Takes a single word string input.

    Returns
    -------
    string
        Titles word if the first letter is a consant. Lowers case of word otherwise.

    """
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

#%%
# Exercise 5
# Define a function to accept a tip percentage, bill total, and
# return the amount to tip
def calculate_tip(bill, tip_perc = 0.2):
    """
    Returns the amount to tip based on the bill.

    Parameters
    ----------
    tip_perc : float
        Expects a percentage in decimal format (e.g. 20% would be 0.20).
    bill : int or float
        Expects a numerical value that can be either an integer or a float.

    Returns
    -------
    float or int
        Multiplies the two arguments together and returns the result.

    """
    return round(tip_perc * bill,2)
    
assert calculate_tip(20,0.2) == 4
assert calculate_tip(30,0.13) == 3.9
assert calculate_tip(20,0.25) == 5

#%%
# Exercise 6
# Define a function to accept an original price, discount percent, and 
# returns the prices after discount is applied
def apply_discount(price,discount):
    """
    Returns the discounted price.

    Parameters
    ----------
    price : integer or float
        Expects a numerical value that can be either an integer or float.
    discount : float
        Expects a percentage in decimal format (e.g. 20% would be 0.20).

    Returns
    -------
    float or int
        Returns sum of price and price multiplied by discount.

    """
    return round(price-(price*discount),2)

assert apply_discount(50, .10) == 45
assert apply_discount(79.99, .2) == 63.99
print('Exercise 6 is correct')

#%%
# Exercise 7
def handle_commas(num_string):
    """
    Returns a number without any commas in it

    Parameters
    ----------
    num_string : string
        Expects a number formatted as a string.

    Returns
    -------
    int
        Returns the integer of given number (but without any commas in it).

    """
    return int(num_string.replace(',','_'))

assert handle_commas('1,000') == 1000
assert handle_commas('1,234,567,890') == 1234567890
print('Exercise 7 is correct')

#%%
# Exercise 8
def get_letter_grade(grade):
    """
    Returns a letter grade for an integer given

    Parameters
    ----------
    grade : int
        Expects an integer likely between 0 and 100.

    Returns
    -------
    str
        Based on value given, returns letter grade F-A as string.

    """
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

assert get_letter_grade(79) == 'C'
assert get_letter_grade(84) == 'B'
assert get_letter_grade(15) == 'F'
assert get_letter_grade(99) == 'A'
print('Exercise 8 is correct')

#%%
# Exercise 9
def remove_vowels(string):
    """
    Removes vowels from a given string.

    Parameters
    ----------
    string : str
        Expects a string of any length.

    Returns
    -------
    string : str
        Returns a transformed string containing no vowels.

    """
    vowels = ['a','e','i','o','u']
    
    for vowel in vowels:
        string = string.replace(vowel,'')
        string = string.replace(vowel.upper(),'')
    
    return string

assert remove_vowels('Howard') == 'Hwrd'
assert remove_vowels('Plays') == 'Plys'
assert remove_vowels('Pinochle') == 'Pnchl'
assert remove_vowels('On') == 'n'
assert remove_vowels('The') == 'Th'
assert remove_vowels('Weekend') == 'Wknd'
print('Exercise 9 is correct')       
    
#%%
# Exercise 10
def normalize_name(string):
    """
    Transforms a given string into Python snake case

    Parameters
    ----------
    string : str
        Expects a string of any length.

    Returns
    -------
    string : str
        Returns a string with special characters removed according to Python naming convention.

    """
    # Initialize any variables needed
    lower_alphabet = [chr(ord('a')+i) for i in range(26)]
    
    # Make 5 passes over name to catch outliers
    for i in range(5):
        
        # Remove invalid characters
        for i in string:
            if i.lower() not in lower_alphabet and i != ' ' and not i.isdigit():
                string = string.replace(i,' ')
        
        # Remove any numbers from leading edge of name
        while True:
            if string[0].isdigit():
                string = string[1:len(string)]
            else:
                break
        
        # Remove extra spaces in between values
        string = ' '.join(string.split())
        
        # Replace spaces with underscores and make sure it's lower case
        string = string.lower().replace(' ','_')
    
    return string

assert normalize_name('%# var name 10') == 'var_name_10'
assert normalize_name('agATHa&*49  ') == 'agatha_49'
assert normalize_name('  495 %3 uLT-vaR 10&^  ') == 'ult_var_10'
print('Exercise 10 is correct')

#%%
# Exercise 11
def cumulative_sum(numbers):
    """
    Given a list of numbers, returns a list of numbers with each subsequent number
    added to the previous.
    EXAMPLE: [1,2,3] becomes [1,3,6]

    Parameters
    ----------
    numbers : list
        Expects a list of numbers as input.

    Returns
    -------
    new_numbers : list
        Returns a list of numbers that are summed cumulatively.

    """
    curr_sum = 0
    new_numbers = []
    
    for i in numbers:
        curr_sum += i
        new_numbers.append(curr_sum)

    return new_numbers

assert cumulative_sum([1,2,3,4]) == [1,3,6,10]
assert cumulative_sum([1,1,1]) == [1,2,3]
assert cumulative_sum([2,4,8,16]) == [2,6,14,30]
print('Exercise 11 is correct')

#%%
### Additional Exercise

# - Once you've completed the above exercises, 
# follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.

### Bonus

#%%
# Bonus 1
def twelveto24(time, reverse = False):
    if reverse == False:
        # Store 
        pass
    
    
    
