'''
Created on 2016. 4. 13.

@author: David
'''
import app2

class MyClass(object):
    '''
    classdocs
    '''
    
    app2.emit
    x = app2.io
    x.emit('response', 'asdf')


    def __init__(self, init=None):
        self.content = init
    
    def __sub__(self, str):
        
        try:
            for i in str:
                self.content = self.content.replace(i, '')
                return MyClass(self.content)
        except Exception:
            print "I don't know"
        
    
    def Print(self):
        f = open('test.txt', 'w')
        f.write(self.content)
        
        f = open('test.txt', 'r')
        a = f.read()
        print a
        f.close()
        print self.content
        
g = MyClass("abcdefg")

g -= "abc"

g.Print()