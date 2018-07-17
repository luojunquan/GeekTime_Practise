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
