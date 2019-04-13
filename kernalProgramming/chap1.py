# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import os
# BASE_DIR =  os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
# sys.path.append(BASE_DIR)
sys.path.append('.')
from libs.util import for_time

print __name__

if __name__ == '__main__':
    print sys.path
    for_time()
    print 'test finished'