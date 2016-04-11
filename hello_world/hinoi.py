'''
Created on 2016. 4. 11.

@author: David
'''
def hanoi(disk, s=1, e=3):
    if disk:
        hanoi(disk-1, s, 6-s-e)
        print(s, " column" , disk, " circle ", e, " column move")
        hanoi(disk-1, 6-s-e, e)
        
hanoi(4)