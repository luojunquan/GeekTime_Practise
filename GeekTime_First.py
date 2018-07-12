#!/usr/bin/env python
#encoding:UTF-8
#列表
'''
a_list = ['a','b']

a_list.append('c')

print(a_list)

a_list.remove('b')

print(a_list)
'''
####################

#判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
'''
alist = []
for i in range(1,11):
    if (i % 2 == 0):
        alist.append(i*i)
print(alist)
##上下两种方式的结果是一样的：列表推导式
blist = [i*i for i in range(1,11) if i % 2 == 0]
print(blist)
'''

'''
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for z in zodiac_name:
    z_num[z] = 0
'''
###上下两种方式的效果是一样的
#字典推倒式
cz_num = {i:0 for i in chinese_zodiac}
z_num = {z:0 for z in zodiac_name}
###

while True:
    #用户输入月份和日期
    int_year = int(input("请输入年份:"))
    int_month = int(input("请输入月份:"))
    int_day = int(input("请输入日期:"))
    num = 0
    while zodiac_days[num] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        num += 1
    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[zodiac_name[num]] += 1

    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))

    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))

#for方式
'''
for zodiac_num in range(len(zodiac_days)):
    if zodiac_days[zodiac_num] >= (int_month,int_day):
        print(zodiac_name[zodiac_num])
        break
    elif int_month == 12 and int_day > 23:
        print(zodiac_name[0])
        break
'''
#while方式
'''
num = 0
while zodiac_days[num] < (int_month,int_day):
    if int_month == 12 and int_day > 23:
        break
    num += 1
print(zodiac_name[num])
'''
