'''
Created on 2016. 4. 16.

@author: David
'''
from compiler.ast import Node

class Node(object):
    

    def __init__(self, data, next):
        self.data = data
        self.next = next

        
    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data
    
    def set_data(self, d):
        self.data = d
        
    def set_next(self, n):
        self.next = n
        
class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def add(self, d):
        node = Node(d, self.root)
        self.root = node
        self.size += 1
        return True
    
    def remove(self, d):
        node = self.root
        prev = None
        while node:
            if node.get_data() == d: # target is found
                if prev:
                    prev.set_next(node.get_next())
                else:
                    self.root = node.get_next()
                self.size -= 1
                return True
            else:
                prev = node
                node = node.get_next()
            
        return False
            
    def get_result(self):
        node = self.root
        while node:            
            print node.get_data()
            node = node.get_next()
    
link = LinkedList()
link.add("data1")
link.add("data2")
link.add("data3")
link.add("data4")
link.remove("data4")

print link.get_size()
link.get_result()
