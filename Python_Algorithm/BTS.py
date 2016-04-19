'''
Created on 2016. 4. 17.

@author: David
'''

class Node(object):
    def __init__(self, d):
        self.data = d
        self.L = None
        self.R = None
        
    def n_insert(self, d):
        if self.data == d:
            return False
        elif self.data > d:
            if self.L:
                return self.L.n_insert(d)
            else:
                self.L = Node(d)
                return True
        else:
            if self.R:
                return self.R.n_insert(d)
            else:
                self.R = Node(d)
                return True
        
    def n_find(self, d):
        if self.data == d:
            print self.L.data, self.R.data
            return True
        elif self.data > d:
            if self.L:
                return self.L.n_find(d)
            else:
                return False
        else:
            if self.R:
                return self.R.n_find(d)
            else:
                return False
            
    def n_preOrder(self):
        if self:
            print str(self.data)
            if self.L:
                self.L.n_preOrder()
            if self.R:
                self.R.n_preOrder()
                
    def n_postOrder(self):
        if self:
            
            if self.L:
                self.L.n_postOrder()
            if self.R:
                self.R.n_postOrder()
            print str(self.data)
                
    def n_inOrder(self):
        if self:    
            if self.L:
                self.L.n_inOrder()
            print str(self.data)
            if self.R:
                self.R.n_inOrder()
                
        
class Tree(object):
    def __init__(self):
        self.root = None
        
    def insert(self, d):
        if self.root:
            return self.root.n_insert(d)
        else:
            self.root = Node(d)
            return True
        
    def find(self, d):
        if self.root:
            return self.root.n_find(d)
        else:
            return False
        
    def preOrder(self):
        print "preOrder function"
        self.root.n_preOrder()
    
    def postOrder(self):
        print "postOrder function"
        self.root.n_postOrder()
        
    def inOrder(self):
        print "inOrder function"
        self.root.n_inOrder()

bst = Tree()
bst.insert(23)
bst.insert(2)
bst.insert(6)
bst.insert(90)
print bst.insert(90)
print bst.find(23)

bst.postOrder()
bst.preOrder()
bst.inOrder()