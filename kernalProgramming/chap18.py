# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:37:18 2017

@author: lulei1992
"""
import threading
from time import ctime,sleep


class ZrbThread(threading.Thread):

    def __init__(self, func, args=()):
        super(ZrbThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def music(f):
    for i in range(2):
        print "I was listening to music %s. %s" %(f, ctime())
        sleep(1)
    return f


def move(f):
    for i in range(2):
        print "I was at the movies %s! %s" %(f, ctime())
        sleep(5)
    return f


def test():
    new_fea = []

    threads = []
    t1 = ZrbThread(func=music, args=('爱情买卖',))
    t2 = ZrbThread(func=move, args=('阿凡达',))
    threads = [t1, t2]

    for t in threads:
        t.setDaemon(True)
        t.start()
    for res in threads:
        res.join()
        res_fea = res.get_result()
        print res_fea
        new_fea.append(res_fea)
        # new_fea = dict(new_fea, **res_fea)

    print new_fea

    print "all over %s" %ctime()


# t1 = threading.Thread(target=music,args=(u'爱情买卖',))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)

if __name__ == '__main__':
    test()




