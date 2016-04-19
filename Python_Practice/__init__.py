# -*- coding: ms949 -*- 
a = 5
b = 10
 
print a + b

a = 0.1 + 0.1+0.1-0.3

print round(a)

print int(a)

print int('5')

#print int('a') error

print float('8.2')

print 1

print bool(0)

print bool(1)

def hanoi(disk, s=1, e=3):
    if disk:
        hanoi(disk-1, s, 6-s-e)
        print(s, " column" , disk, " circle ", e, " column move")
        hanoi(disk-1, 6-s-e, e)
        
hanoi(2)

a, b = 1, 2

print a, b

a, b = b, a

print a, b

# Function

def times(a, b):
    return a*b

a = times(2, 3)

print a # 6
print times # <function times at 0x02271530>

def intersect(first, second):
    list = []
    for x in first:
        if x in second and x not in list:
            list.append(x)
            
    return list

list1 = "SPAM"
list2 = "EGGP"

list = intersect(list1, list2)
print list

def times2(a = 10, b = 20):
    print a*b
    
times2(5)
times2(3)

def test(*args):
    res = []
    for i in args:
        for j in i:
            if j not in res:
                res.append(j)
                
    return res

print test("HAM", "EGg", "SPAM")

g = lambda x, y : x * y

print g(2, 3)

print (lambda x, y : x * y)(2, 4)

a = 11
print 10 if a is 10 else 20

