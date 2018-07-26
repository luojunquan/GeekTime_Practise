#!/usr/bin/env python
#encoding:UTF-8
## numpy库
'''
import numpy
arr1 = numpy.array([1,2,3])
arr2 = numpy.array([1.2,2.3,3.4])
print(arr1 + arr2)

arr3 = numpy.arange(10)
arr3[5:8] = 10
print(arr3)
arr_slice = arr3[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr3)
'''
## pandas库
from pandas import Series,DataFrame
import pandas as pd
'''
obj2 = Series([4,7,-5,3],index=['d','a','b','c'])

print(obj2)

#单个修改索引
obj2['c'] = 6

print(obj2)

sdata = {'beijing':3500,'shanghai':2000,'shenzheng':"5000"}

#将字典转换成pandas
obj3 = Series(sdata)

print(obj3)

#修改全部obj3的索引
obj3.index = ['bj','sh','sz']

print(obj3)
'''
#一维和多维数组
