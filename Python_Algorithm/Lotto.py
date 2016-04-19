'''
Created on 2016. 4. 16.

@author: David
'''
import random as random
# Lotto number is composed with 7 number including bonus Number
# For example, 1, 22, 33, 45, 32, 10, and bonus number 7
# Number will be stored on list

class Lotto(object):
    def __init__(self):
        list = self.number_generate()
        self.pick_number(list)
    
    def number_generate(self):
        list = []
        for i in range(1, 46):
            list.append(i)
        # 1 ~ 45 number is generated and stored on list variable
        return list
    
    def pick_number(self, list):
        pick_list = []
        
        while len(pick_list) < 7:
            i = random.randrange(0, len(list)-1)
            pick_list.append(list.pop(i))
        
        print pick_list

lotto = Lotto()