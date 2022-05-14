# NJFU-LIB-SEAT-RESERVE
## 南京林业大学图书馆座位预约

![njfulogo](/images/logonew.png)

```python
> 依赖
>    requests
>    json
>    unquote
```

```shell
> $ python main.py
```

```json
> {
>     "userid": "userid",    // 学号
>     "passwd": "password",  // 图书馆登录密码
>     "date": "2022-05-15",  // 预约日期
>     "start": "09:00",      // 预约开始时间
>     "end": "22:00",        // 预约结束时间
>     "seat": "4F-A001",     // 精确预约模式的预约座位
>     "window": true,        // 仅预约窗边座位，true/false
>     "area": false,         // 楼层区域优先级预约模式，true/false
>     "areas": {
>         "二层A区":  5,     // 更改楼层区域后的数字顺序，对应不同的预约优先级
>         "二层B区":  6,
>         "三层A区":  2,
>         "三层B区":  3,
>         "三层C区":  4,
>         "四层A区":  1,
>         "五层A区":  9,
>         "六层":     10,
>         "七层北侧": 11,
>         "三楼夹层": 7,
>         "四楼夹层": 8
>     }
> }
```

#### 预览:
![preview](/images/preview.jpg)

### 此项目仅作为私人座位预约以及学习使用
