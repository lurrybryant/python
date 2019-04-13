# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:41:06 2017

@author: lulei1992
"""

import decimal

def printFun():
    #调用str()
    print 'lulei'
    logFile = open('./data/myLog.txt', 'a')
    # print('fatel output', file=logFile)
    logFile.close()
    print("buzhidao {0}".format('niaiwo'))
    x = input("age:")
    print(int(x) * 2)
    #int long bool float complex
    print(decimal.Decimal('1.1'))
    
def strsFun():
    #字符串 列表[]可以修改，元组()不可以，{}字典
    a = 'this is a pig'
    b = [x for x in a if not x == ' ']
    print(b)
    print(a[-1])
    print(a[2:])
    dict = {1: 1, 2:4, 3: 9}
    for key in dict.keys():
        print(key, dict[key])
    for i in range(len(a)):
        print(i, a[i])
    for i, j in enumerate(a):
        print(i, j)
        
def fileFun():
    #参数是引用传递
    a = open('./data/myLog.txt', 'r')
    for line in a:
        print(line,)
        
if __name__ == '__main__':
    # printFun()
    fileFun()


