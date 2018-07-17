#!/usr/bin/env python
#encoding:UTF-8
#正则表达式
import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
'''
#完全匹配
#取出匹配的第一项
print(p.match('2018-07-17').group(1))
#取出匹配的所有项
print(p.match('2018-07-17').groups())
#取出匹配的每一项
 = p.match('2018-07-17').groups()
print(year)
'''
'''
#搜索匹配
year,month,day = p.search('year2018-07-17day').groups()
print(year)
'''
##时间库
'''
import time
import datetime
#最开始的时间到现在的时间
print(time.time())
print(time.localtime())
print(time.strftime('%y%m%d'))

print(datetime.datetime.now())
new_time = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + new_time)

one_day = datetime.datetime(2008,5,27)
new_date = datetime.timedelta(days = 10)
print(one_day + new_date)
'''
##数学相关库
'''
import random
print(random.randint(1,5))
print(random.choice(['aa','bb','cc']))
'''
import numpy
arr1 = numpy.array([1,2,3])
arr2 = numpy.array([1.2,2.3,3.4])
print(arr1 + arr2)

