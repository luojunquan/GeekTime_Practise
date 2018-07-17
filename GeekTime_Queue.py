#!/usr/bin/env python
#encoding:UTF-8
import random
from queue import Queue
from threading import Thread, current_thread
import time

queue = Queue(5)
#生产者
class ProduceThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者%s 生产了数据 %s'%(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者%s 睡眠了%s 秒' % (name, t))
#消费者
class ConsumerThread(Thread):
    def run(self):
        #获取线程的名字
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            #主要是给join用的,每次get后需要调用task_done,直到所有任务都task_done,join才取消阻塞
            queue.task_done()
            print('消费者%s 消费了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('消费者%s 睡眠了%s 秒' % (name, t))

p1 = ProduceThread(name='p1')
p1.start()
p2 = ProduceThread(name='p2')
p2.start()
c1 = ConsumerThread(name='c1')
c1.start()