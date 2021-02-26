text_list = ['1', '2', '3', '6', '5', '6', '6', '2', '1', '5', '5']

# result = max(set(text_list), key=text_list.count)
# print(result)
# 求最多的数
def find_max(list):
    num = 0
    value2 = []
    for i in list:
        if list.count(i) >= num:
            num = list.count(i)
    for i in list:
        if list.count(i) == num:
            value2.append(i)
    value = set(value2)
    return value, num

    # 求最多的数


def find_two_max(list_list):
    num = 0
    value2 = []
    list2 = []
    for i in list_list:
        list2.append(list_list.count(i))
        index = sorted(list2)
    num = list(set(index))[-2]
    for i in list_list:
        if list_list.count(i) == num:
            value2.append(i)
    value = set(value2)
    return value


if __name__ == '__main__':
    print(find_two_max(text_list))
