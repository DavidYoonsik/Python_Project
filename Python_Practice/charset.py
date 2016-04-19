# -*- coding: utf8 -*-
 
# �����ڵ�� �ٷ�� ����1
hoo = unicode('한글', 'utf-8')
print hoo
print str(hoo.encode('utf-8'))
 
# �����ڵ�� �ٷ�� ����2
bar = '한글'.decode('utf-8')
print bar
print bar.encode('utf-8')
 
# �����ڵ�� �ٷ�� ����3
foo = "\uc720\uc724\uc2dd"
print str(foo.decode('utf-8'))