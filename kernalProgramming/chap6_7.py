# -*- coding: utf-8 -*-
from __future__ import division

if __name__ == '__main__':
    a = 999L
    b = repr(0xFF)
    c = str(0XFF)
    d = type(0XFF)

    s = 'abcde'
    for i in [None]+range(-1,-len(s),-1):
    	print s[:i]

