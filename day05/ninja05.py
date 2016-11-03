#!/usr/bin/env python3
#-*- coding:utf-8 -*-

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
## To test the your result
##
## python3 -m doctest -v filename.py

"""
0. Use doctest to see if you are right or not? (This is an example exercise)

Doctest is a common test technique, reference:
  https://docs.python.org/3/library/doctest.html?highlight=doctest#module-doctest

Write the test code begin with '>>>', just like you did in python interactive shell. Then write the expected result
line immediately in next line

For example, given an exercise to create a list l containing 1 through 10

Our test code is following
>>> l  # doctest: +NORMALIZE_WHITESPACE
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Answer code to the exercise is written bellow (outside this doc string):
l = list(range(1,11))

Run the test in terminal and you will see the test passed:
$ python3 -m doctest -v ninja05.py
Trying:
    l  # doctest: +NORMALIZE_WHITESPACE
Expecting:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ok
bla bla...

Now, given an exercise to sum up the list l to s
Our test code is following:
>>> s
55

Run the test again. Because s haven't been computed, you will see the test failed:
$ python3 -m doctest -v ninja05.py
bla bla ...
Trying:
    s
Expecting:
    55
**********************************************************************
File "/Users/david/Workspaces/ShadowTechnology/python-programming/day05/ninja05.py", line 50, in ninja05
Failed example:
    s
Exception raised:
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/doctest.py", line 1320, in __run
        compileflags, 1), test.globs)
      File "<doctest ninja05[1]>", line 1, in <module>
        s
    NameError: name 's' is not defined
bla bla ...

Now, do the exercise by writting code below (outside the doc string):
s = sum(l)

Run the test again, you will see the test passed. We will keep using this technique to write instructions and give you
a sense how the result should look like.
"""
l = list(range(1,11))
# paste the code below this line




__doc__ += \
"""
1. dict exercise
Create dict a, b as following

>>> a  # doctest: +NORMALIZE_WHITESPACE
{1: 'david', 2: 'peter', 3: 'vivi', 4: 'emma'}

>>> b  # doctest: +NORMALIZE_WHITESPACE
{'peter': {'ninja01': 99, 'ninja02': 90}, 'vivi': {'ninja01': 95, 'ninja02': 85},
'david': {'ninja01': 50, 'ninja02': 77}, 'emma': {'ninja01': 92, 'ninja02': 89}}

Create list c as following

"""