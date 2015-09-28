__author__ = 'Sun'
# -*- coding:utf-8 -*-

# name=raw_input('Please enter your name:\n')
# print name

print ord('A')
print(65)

print u'ABC'
print len(u'ABC')
print 'age:%s' % '36'

sum = 0
for x in range(101):
    sum = sum + x
print sum

d = {}
d['Adam'] = 67
print d

print 'Tom' in d

print d.get('Tom', -1)

print cmp(1, 2)
print cmp(2, 1)
print cmp(2, 2)


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    if x < 0:
        return -x


#print my_abs('A')

import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y+step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
r=move(100,100,60,math.pi/6)
print x,y
print r

#函数递归
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print fact(100)