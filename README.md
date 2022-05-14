# NJFU-LIB-SEAT-RESERVE
## 南京林业大学图书馆座位预约

![njfulogo](/images/logonew.png)

> 依赖

```p
    requests
    json
    unquote
```

>```shell
>$ python main.py --help
>
>	Usage:
>		自动预约模式：
>			-a	自动预约模式
>			--id	学号
>			--pwd	密码
>			--day	日期（xxxx-xx-xx）
>			--start	预约开始时间（可选|默认8:00）
>			--end	预约结束时间（可选|默认20:00）
>			--wins	仅预约窗户旁的座位
>			--alls	预约所有座位
>		Ex:
>		  -a --id=xxx --pwd=xxx --day=2022-03-27 --start=8:00 --end=20:00 --wins
>
>		配置文件模式：
>			-c	配置文件
>
>		查询模式：
>			-s	查询模式
>			--name	姓名
>			--date	查询日期
>```

#### 预览:
![preview](/images/preview.jpg)

### 此项目仅作为私人座位预约以及学习使用
