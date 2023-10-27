#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:47:43 2023

@author: manelson
"""

# 1.b.
"""
    Create a file named import_exercises.py. Within this file, use from to import the
    calculate_tip funciton directly. Call this function with values you choose and 
    print the result.
"""
from function_exercises import calculate_tip

print(calculate_tip(40.00,.25))

#%%
"""
2. Read about and use the itertools module from the python standard library to help you solve
the followign problems. Note: Many of these functions in this library return an object,
to see the results of the function, cast this object as a list.
"""
import itertools as it

# How many different ways can you combine a single letter from "abc" with either 1,2, or 3?
print(len(list(it.product('abc','123'))))
    
"""
    There are 9 combinations
"""

# How many different combinations are there of 2 letters from "abcd"?
print(len(list(it.combinations('abcd',2))))
"""
    There are 6 combinations
"""

# How many different permutations are there of 2 letters from "abcd"?
print(len(list(it.permutations('abcd',2))))
"""
    There are 12 different permutations
"""


#%%
"""
    3. Save <specified file> as profiles.json inside of your exercises directory.
    Use the load function from the json module to open this file.
    Your code should produce a list of dictionaries. Using this data, write some code
    that calculates and outputs the following information:
"""
import pprint as pp
import statistics as s
import json
profiles = json.load(open('profiles.json'))

#%%
    # Total number of users
print(f'Total number of users: {len(profiles)}')

#%%
    # Number of active users
active = [i for i in profiles if i.get('isActive') == True]
print(f'Total number of active users: {len(active)}')

#%%
    # Number of inactive users
inactive = [i for i in profiles if i.get('isActive') == False]
print(f'Total number of inactive users: {len(inactive)}')

#%%
    # Grand total of balances for all users
# Isolate the balances
str_balance = [i.get('balance') for i in profiles]

# Convert strings into decimals for easier usage
flt_balances = [float(i[1:].replace(',','_')) for i in str_balance]

# Get the total
total_balance = sum(flt_balances)
print(f'Grand total of balances for all users: ${total_balance:,.2f}')

#%%
    # Average balance per user
avg_balance = round(s.mean(flt_balances),2)
print(f'Average balance per user: ${avg_balance:,.2f}')

#%%
    # User with the lowest balance
# Get the smallest value
min_balance = min(flt_balances)
# print(min_balance)

# match smallest balance to their user
for i in profiles:
    if i.get('balance') == f'${min_balance:,.2f}':
        min_balance_user = i

# Print user with lowest balance
print(f'User with lowest balance: {min_balance_user.get("name")}')
#%%
    # User with the highest balance
# Do the reverse of the lowest balance
# Get max value
max_balance = max(flt_balances)

# Match balance to user
for i in profiles:
    if i.get('balance') == f'${max_balance:,.2f}':
        max_balance_user = i

# Print user with highest balance
print(f'User with highest balance: {max_balance_user.get("name")}')


#%%
    # Most common favorite fruit
# Try the group by function
fav_fruits = list(it.groupby([i.get('favoriteFruit') for i in profiles]))
print(fav_fruits)


#%%
    # Least most common favorite fruit


#%%
    # Total number of unread messages for all users

#%%
### Bonus
"""
    Continue to use the list of dictionaries
"""
# Find out how many unique tags there are for all users
# Display a user's name and all of their respective friends
