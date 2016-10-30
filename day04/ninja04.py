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
## 1 Loop exercise 1
## Please print each element in list:
##    value_list = [1,2,3,4,5,6,7,8]
## Output the following format:
##    1. output the length of value_list:
##        length = 8
a = [1,2,3,4,5,6,7,8]
print(len(a))
##    2. output each element:
##        1,2,3,4,5,6,7,8
for number in a:
    print(number)
##    3. output each even element:
##        2,4,6,8
for number in a:
    if number%2 == 0:
        print(number)
##    4. output each odd element:
##        1,3,5,7
for number in a:
    if number%2 == 1:
        print(number)
##    5. output each reversed element
##        8,7,6,5,4,3,2,1
b = reversed(a)
for number in b:
    print(number)
##    6. output the sum of all elements:
##        sum = 36
print(sum(a))
##    7. output the max element of value_list
##        max_value = 8
print(max(a))
##    8. output the min element of value_list
##        min_value = 1
print(min(a))

#################################################################################
## 2 List comprehension exercise 2
##    data = "123,,456,789,,,,34,,,,12"
data1 = "123,,456,789,,,,34,,,,12"
##Output the following format:
##    1. result = [123,456,789,34,12]

#################################################################################
## 3 exercise 3
##    data = [1,3,2,5,4,8,6,7]
##Output the following format
data = [1,3,2,5,4,8,6,7]
##    1. append a element '9'(use append() function)
##       data = [1,3,2,5,4,8,6,7,9]
print(data)
data.append(9)
print(data)
##    2. insert a element '10' at index 2(use insert() function)
##       data = [1,3,10,2,5,4,8,6,7,9]
data.insert(2, 10)
print(data)
##    3. return final element and delete from list(use pop() function)
##       data = [1,3,10,2,5,4,8,6,7]
data.pop(-1)
print(data)
##    4. sort elements in list(use sort() function)
##       data = [1, 2, 3, 4, 5, 6, 7, 8, 10]
data.sort()
print(data)
##    5. reverse elements in list(use reverse() function)
##       data = [10, 8, 7, 6, 5, 4, 3, 2, 1]
data.reverse()
print(data)

##################################################################################
## 4 exercise 4
## use 'while' statement to calculate the sum from 1 to 100
## input:
##    n = 100
##    sum = 0
##    counter = 1
##    while(){...finished by yourself...}
##    print(sum)
## output:
##    sum = 5050
s = 0
i = 1
while i <= 100:
    s += i
    i +=1
print(s)


##################################################################################
## 5 exercise 5
## Please judge the year that you input is leap year
## for example:
##    2000, 1922,2400 is leap year
##    2011, 2013 is not leap year
##
## input:
##    year = int(raw_input('Please enter the year'))
##    ... finished by yourself...
##
year = int(input('please enter the year'))
if year%4 == 0:
    print('%s is leap year' %(year))
else:
    print('%s is not leap year' %(year))
## output:
##    for example : 2000 is leap year.
##                  2011 is not leap year

###################################################################################
## 6 exercise 6
## Please find prime number from list
## input:
##    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
## output:
##    result = [2,3,5,7,11,13,17,19]

c = range(2, 21)
d = range(2, 20)
for i in c:
    for j in d:
        if i % j == 0:
            break
        else:
            print(i)

