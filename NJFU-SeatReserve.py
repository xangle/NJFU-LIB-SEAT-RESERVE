# -*- coding:utf-8 -*-

import requests
import sys
import os
import json
import datetime
from urllib.parse import unquote
import time

global roomID
roomID = {
    '二层A区': 100455344,
    '二层B区': 100455346,
    '三层A区': 100455350,
    '三层B区': 100455352,
    '三层C区': 100455354,
    '四层A区': 100455356,
    '五层A区': 100455358,
    '六层': 100455360,
    '七层北侧': 106658017,
    '三楼夹层': 111488386,
    '四楼夹层': 111488388
}

global all_seat
all_seat = {}
global window_seat
window_seat = {
    '二层A区': [
        '2F-A001',
        '2F-A003',
        '2F-A005',
        '2F-A007',
        '2F-A021',
        '2F-A023',
        '2F-A037',
        '2F-A039',
        '2F-A045',
        '2F-A047',
        '2F-A061',
        '2F-A063',
        '2F-A077',
        '2F-A079',
        '2F-A087',
        '2F-A089',
        '2F-A103',
        '2F-A105',
        '2F-A119',
        '2F-A121',
        '2F-A129',
        '2F-A131',
        '2F-A145',
        '2F-A147',
        '2F-A197',
        '2F-A199',
        '2F-A213',
        '2F-A215',
        '2F-A229',
        '2F-A231',
        '2F-A239',
        '2F-A241',
        '2F-A255',
        '2F-A257',
        '2F-A271',
        '2F-A273',
        '2F-A281',
        '2F-A283',
        '2F-A297',
        '2F-A299',
        '2F-A313',
        '2F-A315',
        '2F-A323',
        '2F-A325',
        '2F-A339',
        '2F-A341',
        '2F-A355',
        '2F-A357',
        '2F-A365',
        '2F-A367',
        '2F-A381',
        '2F-A383',
        '2F-A397',
        '2F-A399',
        '2F-A407',
        '2F-A409',
        '2F-A423',
        '2F-A425'
    ],
    '三层A区': [
        '3F-A001',
        '3F-A003',
        '3F-A005',
        '3F-A007',
        '3F-A009',
        '3F-A011',
        '3F-A013',
        '3F-A015',
        '3F-A017',
        '3F-A019',
        '3F-A021',
        '3F-A023',
        '3F-A025',
        '3F-A027',
        '3F-A029',
        '3F-A031',
        '3F-A135',
        '3F-A137',
        '3F-A139',
        '3F-A141',
        '3F-A143',
        '3F-A145',
        '3F-A147',
        '3F-A149',
        '3F-A151',
        '3F-A153',
        '3F-A155',
        '3F-A157',
        '3F-A159',
        '3F-A161',
        '3F-A163',
        '3F-A165',
        '3F-A167',
        '3F-A169',
        '3F-A171',
        '3F-A173',
        '3F-A175',
        '3F-A177',
        '3F-A179',
        '3F-A181',
        '3F-A183',
        '3F-A185',
        '3F-A187',
        '3F-A207',
        '3F-A209',
        '3F-A223',
        '3F-A225',
        '3F-A233',
        '3F-A235',
        '3F-A249',
        '3F-A251',
        '3F-A265',
        '3F-A267',
        '3F-A275',
        '3F-A277',
        '3F-A291',
        '3F-A293',
        '3F-A307',
        '3F-A309',
        '3F-A317',
        '3F-A319',
        '3F-A333',
        '3F-A335',
        '3F-A349',
        '3F-A351',
        '3F-A359',
        '3F-A361',
        '3F-A375',
        '3F-A377',
        '3F-A391',
        '3F-A393',
        '3F-A401',
        '3F-A403'
    ],
    '四层A区': [
        '4F-A001',
        '4F-A003',
        '4F-A005',
        '4F-A007',
        '4F-A009',
        '4F-A011',
        '4F-A013',
        '4F-A015',
        '4F-A017',
        '4F-A019',
        '4F-A021',
        '4F-A023',
        '4F-A025',
        '4F-A027',
        '4F-A029',
        '4F-A031',
        '4F-A033',
        '4F-A035',
        '4F-A037',
        '4F-A039',
        '4F-A041',
        '4F-A043',
        '4F-A045',
        '4F-A047',
        '4F-A049',
        '4F-A051',
        '4F-A053',
        '4F-A055',
        '4F-A057',
        '4F-A059',
        '4F-A061',
        '4F-A063'
    ],
    '六层': [
        '6F-A001',
        '6F-A003',
        '6F-A005',
        '6F-A007',
        '6F-A009',
        '6F-A011',
        '6F-A013',
        '6F-A015',
        '6F-A017',
        '6F-A019',
        '6F-A021',
        '6F-A023',
        '6F-A025',
        '6F-A027',
        '6F-A029',
        '6F-A031',
        '6F-A033',
        '6F-A035',
        '6F-A037',
        '6F-A039',
        '6F-A041',
        '6F-A043',
        '6F-A045',
        '6F-A047',
        '6F-A121',
        '6F-A123',
        '6F-A125',
        '6F-A127',
        '6F-A129',
        '6F-A131',
        '6F-A133',
        '6F-A135',
        '6F-A137',
        '6F-A139',
        '6F-A141',
        '6F-A143',
        '6F-A145',
        '6F-A147',
        '6F-A149',
        '6F-A151',
        '6F-A153',
        '6F-A155',
        '6F-A157',
        '6F-A159',
        '6F-A161',
        '6F-A163',
        '6F-A165',
        '6F-A167',
        '6F-A169',
        '6F-A171',
        '6F-A173',
        '6F-A175',
        '6F-A297',
        '6F-A299',
        '6F-A301',
        '6F-A303',
        '6F-A305',
        '6F-A307',
        '6F-A309',
        '6F-A311',
        '6F-A313',
        '6F-A315',
        '6F-A317',
        '6F-A319',
        '6F-A321',
        '6F-A323',
        '6F-A325',
        '6F-A327',
        '6F-A329',
        '6F-A331',
        '6F-A333',
        '6F-A335',
        '6F-A337',
        '6F-A339',
        '6F-A341',
        '6F-A343'
    ],
    '三楼夹层': [
        '3FA-001',
        '3FA-003',
        '3FA-005',
        '3FA-007',
        '3FA-009',
        '3FA-011',
        '3FA-013',
        '3FA-015',
        '3FA-017',
        '3FA-019'
    ],
    '四楼夹层': [
        '4FA-001',
        '4FA-003',
        '4FA-005',
        '4FA-007',
        '4FA-009',
        '4FA-011',
        '4FA-013',
        '4FA-015',
        '4FA-017',
        '4FA-019',
        '4FA-021',
        '4FA-023'
    ]
}

class LibSession:
    def __init__(self, mode):
        self.mode = mode
        self.all_seats_info = {}
        self.all_seats = {}
        self.lib_start = ''
        self.lib_end = ''
        self.lib_reserve_begin = '07:00'
        if self.mode == 'auto' or self.mode == 'mannul':
            self.GetInput()

    def GetInput(self):
        if self.mode == 'auto':
            count = 1
            for floor in roomID.keys():
                print('\t----> (%d).%s' % (count, floor))
                count = count + 1
            floor = [x for x in roomID.keys()]
            floor_num = int(input('请输入楼层区域：'))
            self.floor = floor[floor_num - 1]
        else:
            self.stu_id = input('请输入学号：')
            self.pwd = input('请输入密码：')
            self.date = input('请输入预约日期：')
            self.start_time = input('请输入预约开始时间(ex:8:00)：')
            self.end_time = input('请输入预约结束时间(ex:12:30)：')
            self.seat_name = input('请输入要预约的座位：')

    '''
    延时预约，早上07:02开始预约
    '''
    def DelayReserve(self, date):
        now = datetime.datetime.now()
        date = datetime.datetime.strptime(date + ' ' + self.lib_reserve_begin, '%Y-%m-%d %H:%M')
        if date.day - now.day == 2:
            sleep_time = (date - now).seconds + 121
            print('预约日期%s，将于%s后预约' % (date.strftime('%Y-%m-%d'), \
                                                                     datetime.timedelta(seconds = sleep_time)))
            for i in range(sleep_time):
                time.sleep(1)

    '''
        自动预约：
    '''
    def AutoReserve(self, stu_id, pwd, date, start, end):
        print('将优先预约%s的座位' % (self.floor))
        timedstart = datetime.datetime.strptime(date + ' ' + start, '%Y-%m-%d %H:%M')
        timedend = datetime.datetime.strptime(date + ' ' + end, '%Y-%m-%d %H:%M')
        # 登录
        response, self.login_session = self.LoginLib(stu_id, pwd)
        self.GetStuInfo(response)

        self.count = 0
        floored = []
        def Reserving(date, start, end):
            try:
                while True:
                    # 预约靠窗座位
                    if WINDOW_SEAT:
                        self.seat_name = window_seat[self.floor][self.count]
                    # 预约所有座位
                    if ALL_SEAT:
                        self.seat_name = all_seat[self.floor][self.count]
                    self.count = self.count + 1
                    print('=====> 尝试预约%s的%s...' % (date, self.seat_name))
                    freetime = self.GetFreetime(self.seat_name, date)
                    if freetime == []:
                        continue
                    else:
                        for value in freetime:
                            value[0] = datetime.datetime.strptime(value[0], '%Y-%m-%d %H:%M')
                            value[1] = datetime.datetime.strptime(value[1], '%Y-%m-%d %H:%M')
                            if value[0].hour < timedstart.hour and value[1].hour > timedend.hour:
                                if self.SeatReserve(date, start, end, self.seat_name, self.login_session):
                                    return True
            except IndexError:
                print('=====> [%s无符合条件座位可预约！]' % (self.floor))

        is_reserved = Reserving(date, start, end)
        floored.append(self.floor)
        for self.floor in window_seat.keys():
            self.count = 0
            if is_reserved:
                break
            is_reserved = Reserving(date, start, end)
            if self.floor in floored:
                floored.append(self.floor)
                continue

    '''
        手动预约：
        需手动输入座位，日期，时间段
    '''
    def MannuallyReserve(self):
        self.GetAllSeatsInfo(self.date)
        self.DelayReserve(self.date)
        response, self.login_session = self.LoginLib(self.stu_id, self.pwd)
        self.GetStuInfo(response)
        self.reserved, self.seat_id = self.GetSeatInfo(self.seat_name, self.date, False)
        self.SeatReserve(self.date, self.start_time, self.end_time, self.seat_name, self.login_session)

    '''
        登录图书馆
    '''
    def LoginLib(self, stu_id, pwd):
        login_url = 'http://libic.njfu.edu.cn/ClientWeb/pro/ajax/login.aspx'
        login_params = {
    		'id': stu_id,
    		'pwd': pwd,
    		'act': 'login'
    	}

        login_session = requests.session()
        for i in range(3):
            try:
                response = login_session.post(url = login_url, params = login_params).text
                if json.loads(s = response)['msg'] == 'ok':
                    print('登录成功！')
                    return response, login_session
                if json.loads(s = response)['msg'] == '未获取到相关提示信息':
                    print('用户名或密码输入错误！')
                    os._exit(1) # 从系统级终止程序
            except:
                print('登录失败，请检查网络连接！')
                os._exit(1)

    '''
        获取学生基础信息并打印
    '''
    def GetStuInfo(self, response):
        stu_info = json.loads(s = response)

        stu_id = stu_info['data']['id']
        stu_name = stu_info['data']['name']
        stu_dept = stu_info['data']['dept']
        stu_cls = stu_info['data']['cls']
        stu_full_credit = stu_info['data']['credit'][0][2]
        stu_credit_left = stu_info['data']['credit'][0][1]

        print('\t+---------------------------------------+')
        print('\t|          南京林业大学图书馆           |')
        print('\t+---------------------------------------+')
        print('\t|学号：\t\t\t%s\t|' % (stu_id))
        print('\t|姓名：\t\t\t%s\t\t|' % (stu_name))
        print('\t|年级：\t\t\t%s\t\t|' % (stu_cls))
        print('\t|部门：\t\t\t%s|' % (stu_dept))
        print('\t|信用分数：\t\t(%s/%s)\t|' % (stu_credit_left, stu_full_credit))
        print('\t+---------------------------------------+')
        print('\t|\t\t%s\t\t|' % self.lib_start[:-6])
        print('\t+---------------------------------------+')
        print('\t|开馆时间：\t\t\t%s\t|' % self.lib_start[-6:])
        print('\t+---------------------------------------+')
        print('\t|闭馆时间：\t\t\t%s\t|' % self.lib_end[-6:])
        print('\t+---------------------------------------+')

        time.sleep(3)

    '''
        获取所有座位数据
        数据结构：
        self.all_seats_info = {
            '楼层区域': [['座位', '座位id'], ['学生1', '开始时间', '结束时间'], ['学生2', '开始时间', '结束时间'], ...],
             ...
        }
    '''
    def GetAllSeatsInfo(self, date):
        url = 'http://libic.njfu.edu.cn/ClientWeb/pro/ajax/device.aspx'
        for floor, room_id in roomID.items():
            params = {
                'byType':'devcls',
                'classkind':'8',
                'display':'fp',
                'md': 'd',
                'room_id': room_id,
                'cld_name': 'default',
                'date': date,
                'act': 'get_rsv_sta'
            }
            response = json.loads(s = requests.get(url = url, params = params).text)
            self.all_seats_info[floor] = []
            for count_data in range(len(response['data'])):
                seat_name = response['data'][count_data]['devName']
                seat_id = response['data'][count_data]['devId']
                self.all_seats_info[floor].append([[seat_name, seat_id]])
                for count_ts in range(len(response['data'][count_data]['ts'])):
                    owner = response['data'][count_data]['ts'][count_ts]['owner']
                    start = response['data'][count_data]['ts'][count_ts]['start']
                    end = response['data'][count_data]['ts'][count_ts]['end']
                    self.all_seats_info[floor][count_data].append([owner, start, end])

        # 获取所有楼层名:座位名
        for floor, room_id in roomID.items():
            all_seat[floor] = []
            for items in self.all_seats_info[floor]:
                all_seat[floor].append(items[0][0])

        # 图书馆开/闭馆时间
        self.lib_start = response['data'][0]['ops'][0]['date'] + response['data'][0]['ops'][0]['start']
        self.lib_end = response['data'][0]['ops'][0]['date'] + response['data'][0]['ops'][0]['end']

        return self.all_seats_info

    '''
        获取座位的可预约时间段
    '''
    def GetFreetime(self, seat_name, date):
        reserved, seat_id = self.GetSeatInfo(seat_name, date, True)
        begins, ends = [self.lib_start], [self.lib_end]

        # 已预约时间段
        timed = []
        for i in range(len(reserved)):
            for j in range(len(reserved[i][1:])):
                timed.append(reserved[i][j+1])
        timed.insert(0, self.lib_start)
        timed.append(self.lib_end)

        # 空闲时间段
        freetime = []
        count = 0
        for i in range(len(timed)):
            if i % 2 == 0:
                freetime.append([])
                continue
            freetime[count].append(timed[i-1])
            freetime[count].append(timed[i])
            count = count + 1

        # 去重
        for value in freetime:
            if value[0] == value[1]:
                del freetime[freetime.index(value)]

        # 返回可预约时间段 时间段小于三小时即为不可预约
        willreserve = []
        for value in freetime:
            time1 = datetime.datetime.strptime(value[0], '%Y-%m-%d %H:%M')
            time2 = datetime.datetime.strptime(value[1], '%Y-%m-%d %H:%M')
            if (time2.hour - time1.hour) > 2:
                willreserve.append(value)

        return willreserve


    '''
        获取座位的楼层区域信息
    '''
    def GetRoomID(self, seat_name):
        if seat_name[:1] == '2':
            if seat_name[3:4] == 'A':
                room_id = roomID['二层A区']
            else:
                room_id = roomID['二层B区']
        elif seat_name[:1] == '3':
            if seat_name[:4] == '3FA-':
                room_id = roomID['三楼夹层']
            elif seat_name[3:4] == 'A':
                room_id = roomID['三层A区']
            elif seat_name[3:4] == 'B':
                room_id = roomID['三层B区']
            else:
                room_id = roomID['三层C区']
        elif seat_name[:1] == '4':
            if seat_name[:4] == '4FA-':
                room_id = roomID['四楼夹层']
            else:
                room_id = roomID['四层A区']
        elif seat_name[:1] == '5':
            room_id = roomID['五层A区']
        elif seat_name[:1] == '6':
            room_id = roomID['六层']
        elif seat_name[:1] == '7':
            room_id = roomID['七楼北侧']
        else:
            print("座位号输入有误！")
            sys.exit(0)

        return room_id

    '''
        获取座位已预约的时间段和座位id
    '''
    def GetSeatInfo(self, seat_name, date, printing):
        reserved = []
        for floor in roomID.keys():
            capacity = len(self.all_seats_info[floor])
            for num in range(capacity):
                if self.all_seats_info[floor][num][0][0] == seat_name:
                    seat_id = self.all_seats_info[floor][num][0][1]
                    for i in range(len(self.all_seats_info[floor][num]) - 1):
                        reserved.append(self.all_seats_info[floor][num][i+1])

        if printing:
            # 打印当前座位预约信息
            print('当日已预约(%s)：' % (date))
            for owner in reserved:
                print('    >>>>>> %s: %s～%s' % (owner[0], owner[1][-5:], owner[2][-5:]))

        return reserved, seat_id

    '''
        根据姓名查找
    '''
    def FindByName(self, name):
        seat = ''
        for floor, room_id in roomID.items():
            for items in self.all_seats_info[floor]:
                seat = items[0][0]
                for item in items:
                    if name in item:
                        seat = [seat]
                        seat.append(item)
                        print(seat)
                        break


    '''
        预约座位
    '''
    def SeatReserve(self, date, start, end, seat, login_session):
        reserved, seat_id = self.GetSeatInfo(seat, date, False)
        # 格式化预约时间段
        if len(start) == 4:
            start = '0' + start
        if len(end) == 4:
            end = '0' + end
        start_time, end_time = start[:2] + start[3:], end[:2] + end[3:]
        if start[3:] == '30':
            start = date + '+' + start[:2] + '%' + '3A30'
        else:
            start = date + '+' + start[:2] + '%' + '3A00'
        if end[3:] == '30':
            end = date + '+' + end[:2] + '%' + '3A30'
        else:
            end = date + '+' + end[:2] + '%' + '3A00'

        reserve_url = 'http://libic.njfu.edu.cn/ClientWeb/pro/ajax/reserve.aspx'
        reserve_params = {
            'dev_id': seat_id,
            'start': start,
            'end': end,
            'start_time': start_time,
            'end_time': end_time,
            'act': 'set_resv'
        }
        response = requests.get('http://www.baidu.com', params = reserve_params) # 借用baidu对url转码
        reserve_url = reserve_url + unquote(response.url)[21:]
        response = login_session.get(url = reserve_url)
        response = json.loads(s = response.text)
        if '成功' in response['msg']:
            print('预约座位成功: %s %s %s～%s' % (seat, date, start_time[:2] + ':' + start_time[2:], \
                                                        end_time[:2] + ':' + end_time[2:]))
            return True
        elif '冲突' in response['msg']:
            print("预约座位%s失败，%s！" % (seat, response['msg']))
            return False
        else:
            print("预约座位%s失败，%s！" % (seat, response['msg']))
            sys.exit(0)

def Usage():
    print('\tUsage:')
    print('\t\t自动预约模式：')
    print('\t\t\t-a\t自动预约模式')
    print('\t\t\t--id\t学号')
    print('\t\t\t--pwd\t密码')
    print('\t\t\t--day\t日期（xxxx-xx-xx）')
    print('\t\t\t--start\t预约开始时间（可选|默认8:00）')
    print('\t\t\t--end\t预约结束时间（可选|默认20:00）')
    print('\t\t\t--wins\t仅预约窗户旁的座位')
    print('\t\t\t--alls\t预约所有座位')
    print('\t\tEx:')
    print('\t\t  -a --id=xxx --pwd=xxx --day=2022-03-27 --start=8:00 --end=20:00 --wins')
    print('\n')
    print('\t\t手动预约模式：')
    print('\t\t\t-m\t手动预约模式')
    print('\n')
    print('\t\t查询模式：')
    print('\t\t\t-s\t查询模式')
    print('\t\t\t--name\t姓名')


if __name__ == '__main__':
    argvs = sys.argv[1:]
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
            elif 'day' in value:
                date = value[6:]
            elif 'start' in value:
                start = value[8:]
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
        auto_lib = LibSession('auto')
        auto_lib.DelayReserve(date)
        auto_lib.GetAllSeatsInfo(date)
        auto_lib.AutoReserve(stu_id, pwd, date, start, end)
    elif argvs[0] == '-m':
        lib_mannul = LibSession('mannul')
        lib_mannul.DelayReserve(date)
        lib_mannul.MannuallyReserve()
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
        lib = LibSession('search')
        lib.GetAllSeatsInfo(date)
        if name != '':
            lib.FindByName(name)
    elif argvs[0] == '--help':
        Usage()
    else:
        print('参数有误')
        Usage()
