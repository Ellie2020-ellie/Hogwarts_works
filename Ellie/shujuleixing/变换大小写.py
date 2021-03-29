import re
from filecmp import cmp


def first_m():
    x = "hello world"
    print(x.title())


def frist_m_two():
    arr = "hello world".split(" ")
    new_str = f"{arr[0].capitalize()} {arr[1].capitalize()}"
    print(new_str)


# 检查是否是纯数字
def check_digit():
    s1 = "12223".isdigit()
    print(s1)
    s2 = "12223a".isdigit()
    print(s2)


# 翻转字符串
def return_str():
    s1 = "ilovechina"[::-1]
    print(s1)
    print(s1.lower())
    print(s1.upper())


# 去掉首尾空字符串
def strip_function():
    s1 = " adBbdw "
    print(s1.strip())


# 转码 一个编码为GBK的字符串S，要将其转成UTF - 8编码的字符串
def str_encode():
    a = "S".encode("gbk").decode("utf-8", 'ignore')
    print(a)


'''
s = "info:xiaoZhang 33 shandong",
用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']。
(2）a = "你好 中国 "，去除多余空格只留一个空格。'''


def str_split():
    s = "info:xiaoZhang 33 shandong"
    x = re.split(":| ", s)
    print(x)
    a = "你好 中国 "
    y = ''.join(a.split())
    print(y)


if __name__ == '__main__':
    dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

    print("Value : %s" % dict.setdefault('runoob', None))
    print("Value : %s" % dict.setdefault('Google_one', '淘宝'))
    # 该值包含 Taobao
    for k, v in dict.items():
        print(k, v)
