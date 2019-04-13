# -*- coding: utf-8 -*
print __name__
import time
import datetime
import os
import argparse


def for_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--integer', type=int, help='display an integer')
    args = parser.parse_args()
    print(args.integer)
    return args


def for_time():
    print time.localtime()
    print time.mktime(time.localtime())
    print time.strftime("%y-%m-%d %X", time.localtime())


def for_encode(str1):
    e = str1.decode('utf-8')
    print e.encode('utf-8')


def for_datetime():
    a = datetime.date.today()
    print a.__format__('%Y-%m-%d')
    b = datetime.datetime.now()
    print b


def for_os():
    print os.getcwd()
    a = os.getcwd()
    b = os.listdir(a)
    print b
    print os.path.isfile(b[-1])
    print os.linesep
    os.makedirs(r'lulei\psj')
    os.mkdir('test')

















