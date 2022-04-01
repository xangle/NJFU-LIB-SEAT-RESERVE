import global_var

import json
import requests
from datetime import datetime
from urllib.parse import unquote
import time

global roomID
global window_seat
roomID, window_seat = global_var._init()
global all_seat
all_seat = {}
global now
now = datetime.now()

class LibSession:
    '''
        数据结构：
        所有座位预约信息 self.all_seats_info
        self.all_seats_info = {
            '楼层区域': [
                [['座位1', '座位id'], ['学生1', '开始时间', '结束时间'], ['学生2', '开始时间', '结束时间'], ...],
                [['座位2', '座位id'], ['学生1', '开始时间', '结束时间'], ['学生2', '开始时间', '结束时间'], ...],
            ...]
        }
        所有座位已预约时间段 self.reserved
        self.reserved = {
            '座位1': ['座位id', ['开始时间'，'结束时间'], ['开始时间', '结束时间'], ...],
            '座位2': ['座位id', ['开始时间'，'结束时间'], ['开始时间', '结束时间'], ...],
            ...
        }
        所有座位可预约时间段 self.freetime
        self.freetime = {
            '座位1': ['座位id', ['开始时间'，'结束时间'], ['开始时间', '结束时间'], ...],
            '座位2': ['座位id', ['开始时间'，'结束时间'], ['开始时间', '结束时间'], ...],
            ...
        }
    '''
    def __init__(self, mode, date):
        self.all_seats_info = {}
        self.lib_open = ''
        self.lib_close = ''
        self.freetime = {}

        # 目标日期所有座位预约信息
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
        self.lib_open = response['data'][0]['ops'][0]['date'] + response['data'][0]['ops'][0]['start']
        self.lib_close = response['data'][0]['ops'][0]['date'] + response['data'][0]['ops'][0]['end']

        # 目标日期所有座位已预约时间段
        self.reserved = {}
        for floor, seats in self.all_seats_info.items():
            for seat in seats:
                self.reserved[seat[0][0]] = [seat[0][1]]
                for i in range(len(seat)):
                    if i == 0:
                        continue
                    self.reserved[seat[0][0]].append(seat[i][1:])


        # 对已预约信息据时间排序
        for seat, info in self.reserved.items():
            infolen = len(info)
            if infolen < 2:
                continue
            for i in range(1, infolen):
                for j in range(1, infolen):
                    if int(self.reserved[seat][i][0][11:13]) < int(self.reserved[seat][j][1][11:13]):
                        self.reserved[seat][j][0], self.reserved[seat][i][0] = \
                            self.reserved[seat][i][0], self.reserved[seat][j][0]
                        self.reserved[seat][j][1], self.reserved[seat][i][1] = \
                            self.reserved[seat][i][1], self.reserved[seat][j][1]
        # 可预约时间段
        for seat, info in self.reserved.items():
            if len(info) == 2:
                if int(info[1][0][11:13]) - int(self.lib_open[11:13]) < 4 or \
                        int(self.lib_close[11:13]) - int(info[1][1][11:13]) < 4:
                    continue
                self.freetime[seat] = [info[0]]
                self.freetime[seat].append([self.lib_open, info[1][0]])
                self.freetime[seat].append([info[1][1], self.lib_close])
            if len(info) == 1:
                self.freetime[seat] = [info[0], [self.lib_open, self.lib_close]]

    '''
        获取用户输入
    '''
    def GetInput(self):
        if self.mode == 'auto':
            count = 1
            for count, floor in enumerate(roomID.keys()):
                print('\t----> (%d).%s' % (count, floor))
            floor = [x for x in roomID.keys()]
            floor_num = int(input('请输入楼层区域：'))
            floor = floor[floor_num - 1]
            return floor
        else:
            self.stu_id = input('请输入学号：')
            self.pwd = input('请输入密码：')
            self.date = input('请输入预约日期：')
            self.start_time = input('请输入预约开始时间(ex:8:00)：')
            self.end_time = input('请输入预约结束时间(ex:12:30)：')

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

        print('正在登录%s' % stu_id)
        login_session = requests.session()
        for i in range(3):
            try:
                response = login_session.post(url = login_url, params = login_params).text
                if json.loads(s = response)['msg'] == 'ok':
                    print('登录成功！')
                    break
                if json.loads(s = response)['msg'] == '未获取到相关提示信息':
                    print('用户名或密码输入错误！')
                    os._exit(1) # 从系统终止程序
            except:
                print('登录失败，请检查网络连接！')
                os._exit(1)

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
        print('\t|\t\t%s\t\t|' % self.lib_open[:-6])
        print('\t+---------------------------------------+')
        print('\t|开馆时间：\t\t\t%s\t|' % self.lib_open[-6:])
        print('\t+---------------------------------------+')
        print('\t|闭馆时间：\t\t\t%s\t|' % self.lib_close[-6:])
        print('\t+---------------------------------------+')

        return login_session

    '''
        获取座位已预约时间信息
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
        自动预约座位
    '''
    def AutoReserve(self, stu_id, pwd, date, start, end, WINDOW_SEAT, ALL_SEAT):
        login_session = self.LoginLib(stu_id, pwd)
        for floor in self.all_seats_info.keys():
            if WINDOW_SEAT:
                if floor not in window_seat.keys():
                    continue
                print('=====> 尝试预约%s' % floor)
                for seat_name in window_seat[floor]:
                    if seat_name not in self.freetime.keys():
                        continue
                    if int(start[:2]) >= int(self.freetime[seat_name][1][0][11:13]) and \
                            int(end[:2]) <= int(self.freetime[seat_name][1][1][11:13]):
                        if self.SeatReserve(date, start, end, seat_name, login_session):
                            return None
                    if int(start[:2]) >= int(self.freetime[seat_name][1][0][11:13]) and \
                            int(end[:2]) <= int(self.freetime[seat_name][1][1][11:13]):
                        if self.SeatReserve(date, start, end, seat_name, login_session):
                            return None
            if ALL_SEAT:
                for seat_name in all_seat[floor]:
                    if self.SeatReserve(date, start, end, seat_name, login_session):
                        return None
            print('=====> [%s无符合条件座位可预约！]' % (floor))

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
        elif '不得再预约' in response['msg']:
            print("预约座位%s失败，%s！" % (seat, response['msg']))
            return True

    '''
        查找
    '''
    def FindByName(self, name):
        seat = ''
        for floor, room_id in roomID.items():
            for items in self.all_seats_info[floor]:
                seat = [items[0][0]]
                for item in items:
                    if name in item:
                        seat.append(item)
                        print(seat)
