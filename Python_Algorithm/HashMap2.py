'''
Created on 2016. 4. 20.

@author: David
'''

class Node():
    def __init__(self, key, value):
        self.size = 15
        self.key = self.get_hash(key)
        self.value = value
    
    def get_hash(self, key):
        hash_value = 0 # �ʱ� key ���� �����ϱ� ���� �����Ѵ�.
        for char in str(key):
            hash_value += ord(char)
        return hash_value%self.size