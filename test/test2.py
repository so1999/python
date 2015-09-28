__author__ = 'Sun'
import time

print time.localtime()

timeformat='%Y-%m-%d %H:%M:%S'

now=time.strftime(timeformat,time.localtime())

print now
