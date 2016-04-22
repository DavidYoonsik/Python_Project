class quick_sort():
    #staticmethod(prints)
    
    def sort_main(self, list, first, last):
        if first < last:
            split = self.split_main(list, first, last)
            self.sort_main(list, split+1, last)
            self.sort_main(list, first, split-1)
    
    def split_main(self, list, first, last):
        P = list[first]
        L = first+1
        R = last
        
        while True:
        
            while L <= R and list[L] <= P:
                L += 1
            while L <= R and list[R] >= P:
                R -= 1
                
            if R < L:
                break
            else:
                tmp = list[R]
                list[R] = list[L]
                list[L] = tmp
                print list
                
        tmp = P
        list[first] = list[R]
        list[R] = tmp
                
        print list
        
        return R
        
        
list = [5, 8, 4, 1, 9, 5, 8, 4, 1, 5, 8, 4, 1]
first = 0
last = len(list) - 1



x = quick_sort()
x.sort_main(list, first, last)