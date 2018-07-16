#!/usr/bin/env python
#encoding:UTF-8
'''
import re
def find_main_charecters(charecter_name):
    with open('sanguo.txt',encoding='utf-8') as f:
        data = f.read().replace("\n","")
        name_num = re.findall(charecter_name,data)
    return charecter_name,len(name_num)

#人名文件
name_dict = {}
with open('name.txt',encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            char_name,char_number = find_main_charecters(n)
            print('------->' + char_name,char_number)
            name_dict[char_name] = char_number
            # for key in name_dict.keys():
            #     print('==='+key)

#武器文件
weapon_dict = {}
with open('weapon.txt',encoding='utf-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            weapon_name,weapon_number = find_main_charecters(line.strip())
            print(weapon_name,weapon_number)
            weapon_dict[weapon_name] = weapon_number
        i += 1

name_sorted = sorted(name_dict.items(),key = lambda item:item[1],reverse=True)

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
'''

def counter(FIRST=0):
    cnt = [FIRST]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num5 = counter(5)
num10 = counter(10)

print(num5())
# print(num5())
# print(num5())
# print(num10())
# print(num10())