#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 19.

@author: David
'''

# Key and Value Pair
# No duplicate key

class HashMap():
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size
        # 처음 map 의 사이즈를 정해준다. 보통은 15개 정도로...
        
    def get_hash(self, key):
        hash_value = 0 # 초기 key 값을 저장하기 위해 선언한다.
        for char in str(key):
            hash_value += ord(char)
        return hash_value%self.size
    
    def add(self, key, value):
        hash_key = self.get_hash(key) # 해쉬함수를 이용해 해쉬값을 가져왔다.
        
        hash_value = [key, value] # 키와 값을 리스트로 묶는다.
        
        if self.map[hash_key] is None:
            self.map[hash_key] = list([hash_value])
            return True
        else:
            for pair in self.map[hash_key]: # 근데 key 값이 이미 존재한다면
                if pair[0] == key:
                    pair[1] = value # Update를 해주고
                    return True
            self.map[hash_key].append(hash_value) # 아니라면 새로운 키값을 이용해 HashMap에 집어 넣는다
            return True
        
    def get(self, key):
        hash_key = self.get_hash(key)
        
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        hash_key = self.get_hash(key)
        
        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
            
    def prints(self):
        for i in self.map:
            print '-------------------------'
            if i is not None:
                for j in i:            
                    print j[0], j[1]
                
                
h = HashMap()
h.add('사랑짱', '1111-2222')
h.add('냉장고', '2222-2222')
h.add('를', '3333-2222')
h.add('부탁해', '4444-2222')
h.add('무한', '5555-2222')
h.add('도전', '3333-2222')
h.add('님과', '4444-2222')
h.add('함께', '3333-2222')
h.add('식신', '4444-2222')
h.add('로드', '3333-2222')
h.add('일박이일', '4444-2222')
h.add('판타스틱', '3333-2222')
h.add('듀', '4444-2222')
h.prints()