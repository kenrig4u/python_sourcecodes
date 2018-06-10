# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:05:28 2018

@author: SilverDoe
"""

# lists are ordered mutable sequences

a = ['mango','papaya','strawberry','cherry']
b = ['mango',1,'papaya',4,6,'strawberry',9,'cherry']

a[0]=12


print(a)

c = a[2] # return the value at 2nd index from the list a
print(c)
print(c[2]) # return the value at the 2nd index of the variable c

d = a[2][2]
print(d)


e = 'mango' in b
print(e)
f = 9 in b
print(f)
g = 8 in b
print(g)


listt = a+b # adding two lists
print(listt) 

for item in b:
    print(item)

# Lists building by comprehension :

A = [x for x in range(2,10,2)] # iteration results ae used to populate the list A


