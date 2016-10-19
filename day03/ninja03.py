#!/usr/bin/env python3

## !NOTE! It's good to write shell bang for your script, remember how to write it!

## INSTRUCTIONS:
##
## Finish the following ninja practices
## To run this script make sure to add execute permission to the script, e.g.
##
##   $ chmod u+x <filename>.py
##
## Then run with this script with
##
##   $ ./<filename>.py
##

################################################################################
## 1 List1
## Take the following information as inputs:
##    fruits = ['Apple', 'Banana', 'Peach', 'Grape', 'Plum' ,'Lemon', 'Pear']
## Output the following lines:
##    1. Apple
fruits = ['Apple', 'Banana', 'Peach', 'Grape', 'Plum', 'Lemon', 'Pear']
print(fruits[0])
##    2. Banana
print(fruits[1])
##    3. Pear
print(fruits[-1])

##    4. Apple, Banana, Peach
print(fruits[0:3])
##    5. Peach, Grape,Plum
print(fruits[2:5])
##    6. Plum, Lemon, Pear
print(fruits[-3:])

################################################################################
## 2 List2
## Take the following information as inputs:
##    L = [
##        ['facebook, 'linkedin', 'amazon', 'google'],
##        ['Java','Python', 'Php'],
##        ['Bob','Tom','Jack']
##        ]
## Output the following lines:
##    1. facebook
L = [['facebook','linkedin', 'amazon', 'google'], ['Java', 'Python', 'Php'], ['Bob', 'Tom', 'Jack']]
print(L[0][0])

##    2. Python
print(L[1][1])
##    3. Jack
print(L[2][2])

################################################################################
## 3 Tuple1
## Take the following information as inputs:
##    classmates = ('Michael', 'Jack', 'Tom', 'Bob')
## Output the following lines:
##    1. Michael
classmates = ('Micheal', 'Jack', 'Tom', 'Bob')
print(classmates[0])
##    2. Bob
print(classmates[-1])
##    3. Jack,Tom
print(classmates[1:3])
##v   4. Tom,Bob
print(classmates[-2:])

################################################################################
## 4 Tuple2
## Take the following information as inputs:
##    classmates = ('Michael', 'Jack', ['Tom', 'Bob'])
## Output the follwing lines:
classmates = ('Michael', 'Jack', ['Tom', 'Bob'])
##    1. Jack
print(classmates[1])
##    2. Tom
print(classmates[2][0])
##    3. Bob
print(classmates[2][1])
##    4. Tom,Bob
print(classmates[2])
## How to change 'Tom' to 'Jason', the classmates output:
##    classmates = ('Michael', 'Jack', ['Jason', 'Bob'])
classmates[2][0] = 'Jason'
print(classmates)

################################################################################
## 5 Find more built-in functions
## Python provide a bunch of built-in functions for your convenience, we've seen
## some of them:
##   int(), float(), str(), bool()  # convert variable type to int/float/string/bool
##   len()  # get length of a list or string
##   type()  # get type of a variable
##   input()  # get user input (stdin)
##   print()  # print object to standard output (stdout)
##   bin(), oct(), hex()  # convert a integer to binary/octal/hexical representation string
##   abs()  # get absolute value
##   max(), min()  # get max/min value of two object or a list
##   list(), tuple()  # convert to list/tuple
##
## Now we are going to meet more of them
##   all()  # return True if all elements of list are true
##   any()  # return True if any element of list is true
##   sum()  # sum up
##   sorted()  # reverse the list
##
## You can find the information at:
##   https://docs.python.org/3.5/library/functions.html
## Your task in the part, use the built-in function to find out the following information
##   1. Print result of all(), any() on list [True, False, True, True, False]
Lst1 = [True, False, True, True, False]
print(all(Lst1))
print(any(Lst1))
##   2. Print sum of list [12, 0, -5, -7, 11, 21, 55, -28]
Lst2 = [12, 0, -5, -7, 11, 21, 55, -28]
print(sum(Lst2))
##   3. Print sorted list of [12, 0, -5, -7, 11, 21, 55, -28]
print(sorted(Lst2))
##   4. Print max/min value of [12, 0, -5, -7, 11, 21, 55, -28]
print(max(Lst2))
print(min(Lst2))
##   5. Print length of list [12, 0, -5, -7, 11, 21, 55, -28]
print(len(Lst2))

