#!/usr/bin/env python
#encoding:UTF-8

from __future__ import print_function
import sys,os
'''
#判断文件是否存在
def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + 'does not exists')
    elif not os.access(filename,os.R_OK):
        raise SystemExit(filename + 'is not accessible')
    else:
        print(filename + 'is accessible')

if __name__ == '__main__':
    main()
'''
#通过cat /etc/passwd |python test_argv.py 将调用的内容输出到列表里
'''
def get_content():
    return sys.stdin.readlines()

print(get_content())
'''
'''
1、filename 前正在读取的文件名；
2、fileno ：文件的描述符；
3、filelineno ：正在读取的行是当前文件的第几行；
4、isfirstline ：正在读取的行是否当前文件的第 行；
5、isstdin fileinput：正在读取文件还是直接从标准输入读取内容
'''
'''
import fileinput
for line in fileinput.input():
    # print(line,end='')
    meta = [fileinput.filename(),fileinput.filelineno(),fileinput.fileno(),fileinput.isfirstline(),fileinput.isstdin()]
    print(*meta,end="")
    print(line,end="")
'''
#使用 getpass 库读取密码
'''
import getpass
#主要包含 getuser 函数和 getpass 函数 前者用来从环境变 中获取用户名，后者用来等待用户输入密码
user = getpass.getuser()
passwd = getpass.getpass('your password:')
print(user,passwd)
'''
#使用 ConfigParse 解析配置文件
import ConfigParser
cf = ConfigParser.ConfigParser(allow_no_value=True)
cf.read('/home/python/Desktop/my.cnf.bak')
print(cf.sections)