#!/usr/bin/env python3.9
# -*- coding:utf-8 -*-

import libsession
import sys

def Usage():
    print('\tUsage:')
    print('\t\t自动预约模式：')
    print('\t\t\t-a\t自动预约模式')
    print('\t\t\t--id\t学号')
    print('\t\t\t--pwd\t密码')
    print('\t\t\t--date\t日期（xxxx-xx-xx）')
    print('\t\t\t--start\t预约开始时间（可选|默认8:00）')
    print('\t\t\t--end\t预约结束时间（可选|默认20:00）')
    print('\t\t\t--wins\t仅预约窗户旁的座位')
    print('\t\t\t--alls\t预约所有座位')
    print('\t\tEx:')
    print('\t\t  -a --id=xxx --pwd=xxx --date=2022-03-27 --start=8:00 --end=20:00 --wins')
    print('\n')
    print('\t\t查询模式：')
    print('\t\t\t-s\t查询模式')
    print('\t\t\t--name\t姓名')
    print('\t\t\t--date\t查询日期')

def Command(argvs):
    if argvs == []:
        Usage()
        sys.exit(1)
    if argvs[0] == '-a':
        start, end, WINDOW_SEAT, ALL_SEAT = '8:00', '20:00', False, False
        for value in argvs[1:]:
            if 'id' in value:
                stu_id = value[5:]
            elif 'pwd' in value:
                pwd = value[6:]
            elif 'date' in value:
                date = value[7:]
            elif 'start' in value:
                start = value[8:]
                if len(start) < 5:
                    start = '0'+start
            elif 'end' in value:
                end = value[6:]
            elif 'wins' in value:
                WINDOW_SEAT = True
            elif 'alls' in value:
                ALL_SEAT = True
            else:
                print('参数有误')
                Usage()
                sys.exit(1)
        auto_lib = libsession.LibSession('auto', date)
        auto_lib.AutoReserve(stu_id, pwd, date, start, end, WINDOW_SEAT, ALL_SEAT)
    elif argvs[0] == '-s':
        name, seat = '', ''
        for value in argvs[1:]:
            if '--name=' in value:
                name = value[7:]
            elif '--date=' in value:
                date = value[7:]
            else:
                print('参数有误')
                Usage()
                sys.exit(0)
        print('正在查询...')
        lib = libsession.LibSession('search', date)
        if name != '':
            lib.FindByName(name)
    elif argvs[0] == '--help':
        Usage()
    else:
        print('参数有误')
        Usage()


if __name__ == '__main__':
    Command(sys.argv[1:])
