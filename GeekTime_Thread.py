#!/usr/bin/env python
#encoding:UTF-8
import threading
import time
from threading import current_thread
'''
def myThread(arg1,arg2):
    print(current_thread().getName(),'start')
    print('%s %s'%(arg1,arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')

for i in range(1,6,1):
    #单线程
    #t1 = myThread(i,i+1)
    #多线程
    t1 = threading.Thread(target=myThread,args=(i,i+1))
    t1.start()

print(current_thread().getName(),'end')
'''
#面向对象
class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')

t1 = MyThread()
t1.start()
#主线程和多线程一起结束
t1.join()
print(current_thread().getName(),'end')