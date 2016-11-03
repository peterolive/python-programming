#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 1. Simple open
#f = open('./README.md')
#print(f.read())
#f.close()

# 2. Open a file that is not exist
#f = open('newfile.txt', 'a')
#f.write('banana\n')
#f.close()

# 3. Open real data
f = open('/Users/david/Desktop/data.csv', 'r')

headers = [header.strip('"') for header in f.readline().strip('\n').split(',')]
data = {header: [] for header in headers}

#for line in f:
#    line = line.strip('\n')
#    l = line.split(',')
#    for i, header in enumerate(headers):
#        data[header].append(l[i])

for line in f:
   line = line.strip('\n')
   for header, value in zip(headers, line.split(',')):
       data[header].append(value)

#print(data)

f.close()

# 4. with
with open('newfile.txt', 'r') as f:
    print(f.read())

#print('hahaha')

# 5. function
def getDataDict(file):
    """
    Get data from a CSV file.
    :param file: the file name of the data CSV file
    :return: data dict where use headers as keys and store data in a value list

    >>> data = getDataDict('file.txt')
    file.txt is not a data file.
    """
    if file[-4:] != '.csv':
        print('%s is not a data file.'%(file))
        return None

    with open(file, 'r') as f:
        headers = [header.strip('"') for header in f.readline().strip('\n').split(',')]
        data = {header: [] for header in headers}

        for line in f:
            line = line.strip('\n')
            for header, value in zip(headers, line.split(',')):
                data[header].append(value)

    return data

#d1 = getDataDict('/Users/david/Desktop/data1.csv')
#d2 = getDataDict('/Users/david/Desktop/data2.csv')
