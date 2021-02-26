"""
有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
答:
有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
如果让+等于 0，-等于 1 不就是排序了么。
"""
from collections import deque
from timeit import Timer

s = "++++++----+++----"


# 方法一
def func1():
    new_s = s.replace("+", "0").replace("-", "1")
    result = "".join(sorted(new_s)).replace("0", "+").replace("1", "-")
    print(result)
    return result


#
# 方法二
def func2():
    q = deque()
    left = q.appendleft
    right = q.append
    for i in s:
        if i == "+":
            left("+")
        elif i == "-":
            right("-")


# # 方法三
# def func3():
#     data = list(s)
#     start_index = 0
#     end_index = 0
#     count = len(s)
#     while start_index + end_index < count:
#         if data[start_index] == '-':
#             data[start_index], data[count - end_index - 1] = data[count - end_index - 1], data[start_index]
#             end_index += 1
#         else:
#             start_index += 1
#     return "".join(data)
#
#
if __name__ == '__main__':
    func1()
#     timer1 = Timer("func1()", "from __main__ import func1")
#     print("func1", timer1.timeit(1000000))
#     timer2 = Timer("func2()", "from __main__ import func2")
#     print("func2", timer2.timeit(1000000))
#     timer3 = Timer("func3()", "from __main__ import func3")
#     print("func3", timer3.timeit(1000000))
