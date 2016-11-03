#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# simple funtion
def add(a, b):
    """
    Add two values

    :param a: number a
    :param b: number b
    :return: number a+b
    >>> add(1, 3)
    4
    >>> add('David', 123)
    invalid parameters: a and b should be a number.
    """

    if type(a) != type(0) or type(b) != type(0):
        print('invalid parameters: a and b should be a number.')
    else:
        return a + b

# function parameters
def taxCalculator(income, rate=0.1):
    """
    Calculate tax to pay given income and tax rate.

    :param income: number income
    :param rate: tax rate (default rate is 0.1)
    :return: tax to pay
    >>> taxCalculator(1000, 0.2)
    200.0
    >>> taxCalculator(rate=0.2, income=1000)
    200.0
    >>> taxCalculator(1000)
    100.0
    """

    return income * rate

def mySum(*numbers):
    """
    Calculate sum of parameters

    :param numbers: numbers to sum up! give any length of parameters!
    :return: sum of parameters
    >>> mySum(1,2,3,4)
    10
    >>> mySum(1,2,3,4,5)
    15
    >>> l = [1,2,3,4,5,6,7,8]
    >>> mySum(*l) # mySum(1, 2, 3, 4, 5, 6, 7, 8)
    36
    """
    #s = 0
    #for n in numbers:
    #    s += n
    #return s
    return sum(numbers)


def taxCalculator2(rate=0.1, *incomes): # !NOTE! incomes should comes after rate
    """
    Given a list of incomes and a rate, calculate tax to pay for each of them.

    :return: a list of tax to pay
    >>> taxCalculator2(0.2, 1000, 2000, 3000, 10000)
    [200.0, 400.0, 600.0, 2000.0]
    >>> taxCalculator2(0.2, 1000, 2000, 3000, 10000, 20000)
    [200.0, 400.0, 600.0, 2000.0, 4000.0]
    """

    result = []
    for i in incomes:
        result.append(i*rate)

    return result

def toJSON(**kwargs):
    """
    Given data, return JSON formated string

    Example of JSON formated string:
    {"employee":"David", "Age": 1}

    :param kwargs: key value data
    :return: JSON formated string
    >>> toJSON(employee='David', age=1)
    {"employee":"David", "age": 1}
    >>> toJSON(name='David', income=1000, tax=100, gender='m')
    {"name":"David", "income":1000, "tax"=100, "gender":"m"}
    """
    l = []
    for k, v in kwargs.items():
        l.append('"%s":%s'%(k, v))
    return '{'+', '.join(l)+'}'

def makeEmployeeDict(**kwargs):
    """
    Given employee infomation, return a dict represent an employee

    :param kwargs: employee infomation
    :return: dict of employee information
    >>> makeEmployeeDict(name="David", age=1)
    {'name':'David', 'age':1, 'company':'shadow'}
    >>> makeEmployeeDict(name="David", age=1, gender='m')
    {'name':'David', 'age':1, 'company':'shadow', 'gender'='m'}
    >>> d = {'name':'David', 'age':1}
    >>> makeEmployeeDict(**d)
    {'name':'David', 'age':1, 'company':'shadow'}
    """
    result = dict(kwargs)
    result['company'] = 'shadow'
    return result

# order of parameters left to right
# def fun(normal_params, default_params, *args_params, **kwargs_params):
#   ...


