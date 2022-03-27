# NJFU-LIB-SEAT-RESERVE
## 南京林业大学图书馆座位预约

> 依赖

    import requests
    import json
    import datetime
    from urllib.parse import unquote

```key
$ python SeatReserve.py --help
```

	Usage:
		自动预约模式：
			-a	自动预约模式
			--id	学号
			--pwd	密码
			--day	日期（xxxx-xx-xx）
			--start	预约开始时间（可选|默认8:00）
			--end	预约结束时间（可选|默认20:00）
			--wins	仅预约窗户旁的座位
			--alls	预约所有座位
		Ex:
		  -a --id=xxx --pwd=xxx --day=2022-03-27 --start=8:00 --end=20:00 --wins


		手动预约模式：
			-m	手动预约模式


		查询模式（不可同时查询姓名与座位）：
			-s	查询模式
			--name	姓名
			--seat	座位

