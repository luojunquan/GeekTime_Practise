#!/usr/bin/env python
#encoding:UTF-8

#迭代器
'''
def frange(start,stop,step):
    x = start
    while x < stop:
        yield x
        x += step

for i in frange(10,20,0.5):
    print(i)
'''
from time import sleep

'''
def fab3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
f=fab3(5)
print("f是一个可迭代对象，并没有执行函数")
print(f)
print('fab3返回的是一个iterable 对象，可以用for循环获取值')
for n in f:
    print(n)
'''
'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
           yield b
        # print b
           a, b = b, a + b
           n = n + 1

for i in fab(5):
    print(i)
'''
#杨辉三角
'''
def triangles():
    L = [1]
    while True:
       yield L
       L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
'''
#装饰器
'''
#未带参数
import time
def timmer(func):
    def wepper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("运行时间是%s秒"%(stop_time - start_time))
    return wepper

@timmer
def i_can_sleep():
    time.sleep(3)

i_can_sleep()
'''
'''
#带参数
def new_tips(argv):
    def tips(func):
        def nei(a,b):
            print('start-->%s,%s' %(argv,func.__name__))
            func(a,b)
            print('stop-->')
        return nei
    return tips

@new_tips('new_add')
def add(a,b):
    print(a + b)

add(4,5)
'''



