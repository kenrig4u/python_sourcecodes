# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:31:54 2018

@author: SilverDoe
"""

b = ['mango','strawberry','papaya','orange','grape']

b.append('berry')
print(b)

b.extend("hello")
print(b)

b.insert(0,34)  # insert value 34 at index number 0. The other values in the list will be shifted accordingly
print(b)

print(b.count(34))  # return the count

b.remove("mango")  # deletes the first matching item. If there is no match an error will occur
print(b)

print(b.pop())  # pop method returns the value that is deleted using pop method. deletes the item at the last index
print(b)

print(b.pop(2))  # index can be specified to delete a specific item at a given index


c = ['goku','adith','sasi','arun','jasmine','sam','sylvia']
c.sort()
print(c)

c.reverse()
print(c)

#del c['goku']
#del c['sasi','jasmine']
print(c)

