# -*- coding: cp949 -*-

class login():
    
    x = 10
    
    def __init__(self):
        pass
    
    def staticprintcount():
        print login.x
        
    def classprintcount(cls):
        print cls.x
        
    def login_chk(email, pw):
        print email, pw
    
    sm = staticmethod(staticprintcount)
    cm = classmethod(classprintcount)
    ch = staticmethod(login_chk)

a = login()

a.sm()
a.cm()
a.ch('a', 'b')