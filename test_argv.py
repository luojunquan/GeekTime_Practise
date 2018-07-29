#!/usr/bin/env python
#encoding:UTF-8

# from __future__ import print_function
import hashlib
import sys,os

import datetime
import tarfile

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
#主要包含 getuser 函数和 getpass 函数 前者用来从环境变 中获取用户名'后者用来等待用户输入密码
user = getpass.getuser()
passwd = getpass.getpass('your password:')
print(user,passwd)
'''
#################################################
#使用 ConfigParse 解析配置文件
# python3更改成了小写
'''
1、configparser 中有很多的方法'其中与读取配置文件'判断配置项相关的方法有
2、sections ：返回一个包含所有章节的列表；
3、has_section ：判断章节是否存在；
4、items ：以元组的形式返回所有选项；
5、options ：返回一个包含章节下所有选项的列表；
6、has_option ：判断某个选项是否存在；
7、get、getboolean、getinit、getfloat ：获取选项的值
'''
'''
import configparser
cf = configparser.ConfigParser(allow_no_value=True)
cf.read('my.cnf')
print(cf.sections())
print(cf.has_section('client'))
print(cf.options('mysqld'))
print(cf.get('client','host'))
'''
'''
1、remove_section ：删除一个章节；
2、add_section ：添加一个章节；
3、remote_option ：删除一个选项；
4、set ：添加一个选项；
5、write ：将ConfigParser对象中的数据保存到文件中
'''
'''
cf.remove_section('client')
cf.add_section('lxj')
cf.set('lxj','host','127.0.0.1')
cf.set('lxj','port','3306')
#必须要写入才会生效
cf.write(open('my.cnf','w'))
print(cf.remove_section('DEFAULT'))
#清空除[DEFAULT]之外所有内容
cf.clear()
cf.write(open('my.cnf','w'))
print('DEFAULT' in cf)
cf.remove_option('DEFAULT', 'ForwardX11')
cf.set('DEFAULT', 'ForwardX11', 'no')
print(cf['DEFAULT']['ForwardX11'])
cf.write(open('my.cnf','w'))
'''
#################################################
#使用 argparse 解析命令行参数
'''
使用argparse模块、模仿MySQL 客户端、解析命令行的例子在这个例子中，
我们添加了5个选项，分别是 host、user、password、port、version 其中，
host、user、password 都是必传的参数，因为我们没有指定参数的类型，
所以这几个参数的取值都以字符串的形式保存。对于user、password、port选项，
为了提供易用性，可以使用"-u"、"-P"和"-p"的方式指定参数,port 取值是一个端口号，
因此，我们通过type项告诉 ArgumentParser, port 数的数据类型为整数。
'''
'''
import argparse
def _argparse():
	parser = argparse.ArgumentParser(description='Python-MySQL client')
	parser.add_argument ('--host',action='store',dest='host',required=True, help='connect to host')
	parser.add_argument ('-u','--user', action= 'store',dest='user ',required=True, help=' user for login' )
	parser.add_argument ('-p','--password',action= 'store',dest='password',required=True, help='password to use when connecting to server')
	parser.add_argument ('-P','--port', action='store', dest='port',default=3306,type=int,help='port number to use for connection or 3306 for default ' )
	parser.add_argument ('-v','--version', action='version',version='%(prog)s 0.1')
	return parser.parse_args()
def main() :
	parser = _argparse()
	conn_args = dict(host=parser.host, user=parser.user,password=parser.password, port=parser.port)
	print(conn_args)
if __name__ == '__main__':
	main()
'''
#logging模块
'''
import logging
import logging.config
#配置日志格式
# logging.basicConfig(filename='app.log',level=logging.INFO)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename='app.log'
# )
#引用配置文件的方式
logging.config.fileConfig('logging.cnf')
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
'''
#########################################################
#使用 click 解析命令行参数
'''
1、command ：使函数 hello 成为命令行接口；
2、option ：增加命令行选项；
3、echo ：输出结果，使用 echo 进行输出是为了获得更好的兼容性，因为 Python2中print是一个语句， Python3中 print是一个函数
'''
'''
1、default ：设置命令行参数的默认值；
2、help ：参数说明；
3、type ：参数类型，可以是 string、int、float 等；
4、prompt ：当在命令行中没有输入相应的参数时，会根据 prompt 提示用户输入；
5、nargs ：指定命令行参数接受的值的个数。
'''
'''
import click
@click.command()
@click.option('--count',default=1,help='Number of greetings')
@click.option('--name',prompt='Your name',help='The person to greet')
def hello(count,name):
    for x in range(count):
        click.echo('Hello %s!' %name)

if __name__ == '__main__':
    hello()
######
'''
#设置 prompt为True,就能够交互式地输入密码，设置 hide_input为True ，就可以隐藏我们的命令行输入，设置confirmation_prompt为True，就可以进行密码的两次验证
'''
@click.command()
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypting password to %s' % password.encode('rot13'))

if __name__ == '__main__':
    encrypt()
######
#执行程序，系统会自动进入编辑器
import click
message = click.edit()
print(message,end="")
'''
#####################################
# from prompt_toolkit import prompt
# while True:
#     user_input = prompt('>')
#     print(user_input)
#####################################
#文件的一些操作
'''
upper ：将字符串转换为大写；
lower ：将字符串转换为小写
isupper ：判断字符串是否都为大写
islower ：判断字符串是否都为小写
swapcase ：将字符串中的大写转换为小写、小写转换为大写；
capitalize ：将首字母转换为大写；
istitle ：判断字符串是不是一个标题
'''
'''
yes_or_no = input('Please input yes or no:')
if yes_or_no.lower() == "yes":
    print("continue do something")
else:
    print("exit...")
'''
#####################################
### 判断类方法
'''
1、s.isalpha ：如果字符串只包含字母，并且非空，否则返回 True则返回 False;
2、s.isalnum ：如果字符串值包含字母和数字，并且非空，否则返回True ，否则返回False;
3、s.isspace ：如果字符串值包含 制表符、换行符，并且非空，否则返回True，否则返回False·
4、s.isdecimal ：如果字符串只包含数字字符，并且非空，否则返回True 则返回False
'''
import os
# print([item for item in os.listdir('.') if item.endswith('.txt')])
# print([item for item in os.listdir('.') if item.startswith('Geek')])
# #查找mysql日志所占用磁盘大小
# mysql_logs = [item for item in os.listdir('/var/log/mysql/') if item.startswith('error.log')]
# sum_size = sum(os.path.getsize(os.path.join('/var/log/mysql/',item)) for item in mysql_logs)
# #多少M
# print(sum_size / 1024 / 1024)
##print 函数本身可以通过 sep 参数指定分隔符：
# In [10]: print('root','/root','/bin/bash',sep=':')
# root:/root:/bin/bash
##################################################
from collections import Counter
##统计网站的访问热门资源
'''
c = Counter()
with open('access.log') as f:
    for line in f:
        c[line.split()[6]] += 1

print("Popular resources : {0}" .format(c.most_common(10)))
'''
## 计算网站返回值的比率
'''
d = {}
with open('access.log') as f:
    for line in f:
        key = line.split()[8]
        d.setdefault(key,0)
        d[key] += 1

sum_requests = 0
error_requests = 0

for key,val in d.items():
    if int(key) >= 400:
        error_requests += val
    sum_requests += val

print('error rate:{0:.2f}%'.format(error_requests * 100.0 / sum_requests))
'''
############################################
'''
##format的使用
from collections import namedtuple
Person = namedtuple('Person','name age sex')
xm = Person('Xiaoming',20,'male')
print("{p.name} {p.age} {p.sex} old this year".format(p=xm))
#########################
#字符集编码
Unicode 是表现形式， UTF总是存储形式
name = '罗俊强111111'
with open('data.txt','w',encoding='utf-8') as f:
    f.write(name)
############################
正则表达式
推荐使用变异表达式re_obj = re.compile(pattern)
import re
def main():
    pattern = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    re_obj = re.compile(pattern)
    with open('popd.log') as f:
        for line in f:
            data = re_obj.findall(line)
            if len(data) != 0:
                print(data)

if __name__ == '__main__':
    main()
##############3
data= dict(bob=13000000001,lily=130000000002, robin=130000000003)
index = 0
for key,value in data.items():
    index += 1
    print (index,key,value,sep= ",")

#####
#
# with open('data.txt','w') as f:
#     print(1,2,'hello world',sep=",",file=f)


with open('popd.log') as inf,open('out.txt','w') as outf:
    for line in inf:
        outf.write(" ".join([word.capitalize() for word in line.split()]))
        outf.write("\n")
'''
############################################
import os
'''
print("current directory:",os.getcwd())
path = os.path.abspath(__file__)
print("full path of current file:",path)
print("parent directory of current file:",os.path.abspath(os.path.join(os.path.dirname(path),os.path.pardir)))
'''
'''
1、getatime ：获取文件的访问时间
2、getmtime ：获取文件的修改时间
3、getctime ：获取文件的创建时间
4、getsize  ：获取文件的大小
'''
'''
1、exists ：参数path所指向的路径是否存在
2、sfile ：参数path所指向的路 存在，并且是一个文件；
3、isdir ：参数path所指向的路径存在，并且是一个文件夹；
4、islink：参数path所指向的路径存在，并且是一个链接；
5、ismount：参数path所指向的路径存在，并且是一个挂载点
'''
####用来统计每条命令的出现次数，然后找出出现次数最多的 10 条命令
'''
import os
from collections import Counter
c = Counter()
with open(os.path.expanduser('~root/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]] += 1

print(c.most_common(10))
'''
#walk 返回一个三元组（ dirpath, dimames, filenames ）。其中， dirpath 保存的是当前目录， dimames 是当前目录下的子目录列表， filenames 是当前目录下的文件列表
#查找/opt目录下的所有pak的文件
'''
import os
import fnmatch
files = ['*pak']
matches = []
path = "/opt/"
for root,dirnames,filenames in os.walk(os.path.expanduser(path)):
    for extensions  in files:
        for filename in fnmatch.filter(filenames,extensions):
            matches.append(os.path.join(root,filename))
print(matches)
'''
####################################################
'''
import os
import fnmatch
def is_file_match(filename,patterns):
     for pattern in patterns:
         if fnmatch.fnmatch(filename,pattern):
             return True
     return False
#find_specific_files 函数，该函数接受三个参数，分别是查找的根路径，匹配的文件模式列表和需要排除的目录列表。
#walk 返回一个三元组（ dirpath,dimames,filenames ）.其中,dirpath 保存的是
#当前目录,dimames 是当前目录下的子目录列表,filenames 是当前目录下的文件列表
def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
    for root,dirnames,filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename,patterns):
                yield os.path.join(root,filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)
#查到目录下的所有文件
# for item in find_specific_files('.'):
#     print(item)
#查找目录下最大的十个文件
files = {name:os.path.getsize(name) for name in find_specific_files('.',exclude_dirs=['.git'])}
result = sorted(files.items(),key = lambda d:d[1],reverse = True)[:10]
for i,t in enumerate(result,1):
    print(i,t[0],t[1])
'''
#####################################
##找到目录下的重复文件
'''
import os
import fnmatch
import hashlib
CHUNK_SIZE = 8192
def is_file_match(filename,patterns):
     for pattern in patterns:
         if fnmatch.fnmatch(filename,pattern):
             return True
     return False
#find_specific_files 函数，该函数接受三个参数，分别是查找的根路径，匹配的文件模式列表和需要排除的目录列表。
#walk 返回一个三元组（ dirpath,dimames,filenames ）.其中,dirpath 保存的是
#当前目录,dimames 是当前目录下的子目录列表,filenames 是当前目录下的文件列表
def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
    for root,dirnames,filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename,patterns):
                yield os.path.join(root,filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)

def get_chunk(filename):
    with open(filename) as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            else:
                yield chunk

def get_file_checksum(filename):
    h = hashlib.md5()
    for chunk in get_chunk(filename):
        h.update(chunk)
    return h.hexdigest()

def main():
    sys.argv.append("")
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        raise SystemExit("{0} is not a directory".format(directory))

    record = {}
    for item in find_specific_files(directory):
        checksum = get_file_checksum(item)
        if checksum in record:
            print('find duplicate file: {0} vs {1}'.format(record[checksum], item))
        else:
            record[checksum] = item

if __name__ == '__main__':
    main()
'''
####################################################################
#使用 Python 管理压缩包
##创建一个gz的tar包
'''
import tarfile
with tarfile.open('tafile_add.tar',mode='w:gz') as out:
    out.add('name.txt')
'''
'''
1、getnames ：获取 tar 包中的文件列表；
2、extract ：提取单个文件；
3、extractall ：提取所有文件
'''
##读取tar包，并且提取里面的所有文件
'''
import tarfile
with tarfile.open('tafile_add.tar',mode='r:gz') as out:
    for member_info in out.getmembers():
        out.extractall()
'''
#####备份指定的文件到压缩包中
##备份当前目录下的所有.py结尾的文件
'''
import os
import fnmatch
import hashlib
import datetime
def is_file_match(filename,patterns):
     for pattern in patterns:
         if fnmatch.fnmatch(filename,pattern):
             return True
     return False
#find_specific_files 函数，该函数接受三个参数，分别是查找的根路径，匹配的文件模式列表和需要排除的目录列表。
#walk 返回一个三元组（ dirpath,dimames,filenames ）.其中,dirpath 保存的是
#当前目录,dimames 是当前目录下的子目录列表,filenames 是当前目录下的文件列表
def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
    for root,dirnames,filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename,patterns):
                yield os.path.join(root,filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)

def main():
    patterns = ['*.py']
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = "all_py_{0}.tar.gz".format(now)
    with tarfile.open(filename,'w:gz') as f:
        for item in find_specific_files('.',patterns):
            f.add(item)


if __name__ == '__main__':
    main()
'''
####zip压缩包
# import zipfile
# newzip = zipfile.ZipFile('new.zip','w')
# newzip.write('name.txt')
# newzip.close()

'''
zip file 模块提供的命令行接口包含以下几个选项：
-l ：显示 zip格式压缩包中的文件列表
-c ：创建zip 格式压缩包
-e ：提取zip 格式压缩包
-t ：验证文件是一个有效的 zip 格式压缩包
 python3 -m zipfile -l new.zip
'''
###########################################3
#Python 中执行外部命令
'''
import subprocess
output = subprocess.check_output(['df','-h']).decode('utf-8')
lines = output.split('\n')
#用with方式将输出写到文件中
with open('df.txt','w') as f:
    for line in lines[0:-1]:
        f.writelines(line.split()[0] + '    '+ line.split()[1] + '    '+ line.split()[3] + '\n')
#用print方式将输出写入到文件中
# f = open('df.txt', 'w')
# for line in lines[0:-1]:
#     print(line.split()[0], line.split()[1], line.split()[3],file=f)
# f.close()
'''
'''
##call check call 函数直接将命令的输出结果输出到命令行终端
try:
    output = subprocess.check_output(['df','h'],stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    output = e.output
    print(output.decode('utf-8'))
    code = e.returncode
    print(code)
'''
###################
#subprocess 模块的 Popen类
##函数对 Popen 执行 shell 命令进行封装，封装以后，只要将需要执行的 shell 命令传递给该函数即可
# 当命令执行成功时，将返回命令的退出状态码和标准输出，当命令执行失败时，将返回退出状态码和错误输出
'''
import subprocess
def execute_cmd(cmd):
	p = subprocess.Popen(cmd,
						shell=True,
						stdin=subprocess.PIPE,
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE)
	stdout, stderr = p.communicate()
	if p.returncode != 0:
		return p.returncode, stderr
	return p.returncode, stdout
'''






