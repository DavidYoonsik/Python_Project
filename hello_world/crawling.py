'''
Created on 2016. 4. 1.

@author: Me
'''

from sys import version_info
from _ast import Num

py_ver = version_info[0] > 2
print py_ver

global res

if py_ver:
    #global res
    res = input('What? ')
else:
    #global rse
    res = raw_input('What? ')

print res

for i in range(2, 10):
    for j in range(1, 10):
        print i*j


fruits = ['banana', 'apple',  'mango']

for index in range(len(fruits)):
    print 'Current fruit :', fruits[index]

print "Good bye!"

fruit = [['banana', 'apple',  'mango'], ['banana', 'apple',  'mango'], ['banana', 'apple',  'mango']]

for index in range(len(fruit)):
    for index2 in range(len(fruit[index])):
        print 'Current fruit :', fruit[index][index2]

num = 100
if num == 100:
    print num 
else:
    print 'not'
    
    
import calendar
cal = calendar.month(2016, 4)
print cal