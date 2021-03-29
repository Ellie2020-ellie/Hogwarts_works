'''
1.列举Python中的基本数据类型？
答: Python3中有六个标准的数据类型:字符串(String）、数字(Digit）、列表(List）、元组(Tuple）、集合(Sets）、字典(Dictionary）。

2.如何区别可变数据类型和不可变数据类型
答: 从对象内存地址方向来说
可变数据类型:在内存地址不变的情况下，值可改变(列表和字典是可变类型，但是字典中的key值必须是不可变类型）
不可变数据类型:内存改变，值也跟着改变。(数字，字符串，布尔类型，都是不可变类型）可以通过id()方法进行内存地址的检测。
'''
import datetime
import json

if __name__ == '__main__':
    # import time  # 引入time模块
    #
    # ticks = time.time()
    # print("当前时间戳为:", ticks)
    # localtime = time.localtime()
    # print('time.localtime:', localtime)
    # localtime_one = time.asctime(time.localtime())
    # print('localtime_asctime:', localtime_one)
    #
    # itme_str = time.strftime("%Y-%M-%D %H:%M:%S", time.localtime())
    # print('strftime:', itme_str)
    # # time.strptime(a, "%a %b %d %H:%M:%S %Y")
    # print('strftime_two:', time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # print(itme_str)
    # # 将格式字符串转换为时间戳
    # a = "Sat Mar 28 22:24:24 2016"
    # print(time.mktime(time.localtime()))
    import calendar

    cal = calendar.month(2016, 1)
    print(cal)
    print(calendar.isleap(2021))

