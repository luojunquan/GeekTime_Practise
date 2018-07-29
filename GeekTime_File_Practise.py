#!/usr/bin/env python
#encoding:UTF-8
#文件练习操作
#往文件里写东西
'''
file1 = open('name.txt','w')
file1.write('诸葛亮')
file1.close()

#文件读操作
file2 = open('name.txt')
print(file2.read())
file2.close()

#文件增加内容
file3 = open('name.txt','a')
file3.write('刘备')
file3.close()
'''
#读取文件的每行
file4 = open('name.txt')
for file in file4.readlines():
    print(file)



