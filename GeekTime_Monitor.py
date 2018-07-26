#!/usr/bin/env python
#encoding:UTF-8
#使用 Python 监控 Linux 系统
'''
from __future__ import print_function
from collections import namedtuple


Disk = namedtuple('Disk', 'major_number minor_number device_name'
                          ' read_count read_merged_count read_sections'
                          ' time_spent_reading write_count write_merged_count'
                          ' write_sections time_spent_write io_requests'
                          ' time_spent_doing_io weighted_time_spent_doing_io')


def get_disk_info(device):
    """
    从/proc/diskstats中读取磁盘的IO信息
    $ cat /proc/diskstats
    """
    with open("/proc/diskstats") as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))
    raise RuntimeError("device ({0}) not found !".format(device))


def main():
    disk_info = get_disk_info('sda')

    print(disk_info)

    print("磁盘写次数：{0}".format(disk_info.write_count))
    print("磁盘写字节数：{0}".format(disk_info.write_sections) * 512)
    print("磁盘写延时：{0}".format(disk_info.time_spent_write))


if __name__ == '__main__':
    main()
'''
import psutil
##内存
'''
def bytes2human(n):
    symbols = ('K','M','G','T','P','E','Z','Y')
    prefix = {}
    for i,s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value,s)
    return "%sB" % n


if __name__ == '__main__':
    print(bytes2human(psutil.virtual_memory().total))
'''
##获取挂载点的磁盘
'''
def get_disk_via_mountpoint(mountpoint):
    disk = [item for item in psutil.disk_partitions()
              if item.mountpoint == mountpoint]
    return disk[0].device
print(get_disk_via_mountpoint('/'))
'''
















