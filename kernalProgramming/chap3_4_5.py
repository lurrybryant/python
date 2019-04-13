# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:02:40 2017

@author: lulei1992
"""
#decrease quary
from types import IntType  

def isNum(m):
    if type(m)==types.IntType:
        print("{1} is a number".format(m))
        

if __name__ == '__main__':
    print(types.IntType)

    m = 2
    if type(m) is IntType:
        print 'a'
        
    if isinstance(m, IntType):
        f = 1
        print f