# -*- coding: utf-8 -*-

'''
Created on 2016. 4. 14.

@author: David
'''
#-*- coding: euckr -*- 
class crypto():    
    def convStringToInt(self, str):
        list = [];
        for i in range(len(str)):
            list.insert(i, int(str[i])) # 리스트에서 받아온 문자를 int 타입으로 바꿔준다.
        return list
    
    def convIntoToAscii(self, list):
        text = ''
        for i in range(len(list)):
            text += chr(list[i])            
        return text
    
    def shiftRight(self, list):
        local_list = []
        for i in range(len(list)):
            local_list.insert(i, list[i] >> 1)
        return local_list
    
crypto = crypto()
input = "212.242.214.194.220.206.128.198.222.234.224.194.220.206.92.198.222.218"
input_arr = input.split(".")
print input_arr

list = crypto.convStringToInt(input_arr)
list = crypto.shiftRight(list)
text = crypto.convIntoToAscii(list)

print text
