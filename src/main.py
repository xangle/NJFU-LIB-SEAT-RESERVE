import Lib
import json

import global_var

global roomID
global window_seat
roomID, window_seat = global_var._init()


def getFloorHead(floor):
    if floor == "二层A区":
        return "2F-A"
    elif floor == "二层B区":
        return "2F-B"
    elif floor == "三层A区":
        return "3F-A"
    elif floor == "三层B区":
        return "3F-B"
    elif floor == "三层C区":
        return "3F-C"
    elif floor == "四层A区":
        return "4F-A"
    elif floor == "五层A区":
        return "5F-A"
    elif floor == "六层":
        return "6F-A"
    elif floor == "七层北侧":
        return "7F-A"
    elif floor == "三楼夹层":
        return "3FA-"
    elif floor == "四楼夹层":
        return "4FA-"
    else:
        return None


# 读取Json内容
with open("reserve.json", "r") as f:
    data = json.loads(f.read())
userid = data["userid"]
passwd = data["passwd"]
date = data["date"]
start = data["start"]
end = data["end"]
seat = data["seat"]
area = data["area"]
areas = data["areas"]
window = data["window"]

# 初始化图书馆，获取当日图书馆的所有预约信息
print(">>>> 正在获取图书馆预约数据...")
njfulib = Lib.Lib(date)
freetime = njfulib.getReservedData()

# 单座位精准预约
if not area:
    njfulib.seatReserve(date, start, end, seat, njfulib.loginLib(userid, passwd))

# 如果只预约窗边的座位，那么删除freetime中的非窗边座位
if window:
    window_seats = []
    for floor, seats in window_seat.items():
        for seat in seats:
            window_seats.append(seat)
    keys = list(freetime.keys())
    for key in keys:
        if key not in window_seats:
            freetime.pop(key)

# 楼层区域优先级预约
if area:
    for count in range(1, 12):
        for floor, priority in areas.items():
            if priority == count:
                print("  ---> 正在检查%s有无合适座位..." % floor)
                for seat, infos in freetime.items():
                    if seat[0:4] == getFloorHead(floor):
                        for info in infos[1:]:
                            if int(info[0][-5:-3]) <= int(start[:2]) and int(end[:2]) <= int(info[1][-5:-3]):
                                njfulib.seatReserve(date, start, end, seat, njfulib.loginLib(userid, passwd))
                                exit(0)
