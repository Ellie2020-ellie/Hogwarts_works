def number():
    p = '1, 3, 4'
    y = p.split(',')
    print(y)


def list_():
    a = [1, 2, 3, 8, 2]
    b = [1, 2, 4, 5, 6, 7]
    z = set(a) & set(b)
    x = set(a) ^ set(b)
    print(z)
    print(x)


'''[[1, 2], [3, 4], [5, 6]]一行代码展开该列表，得出[1, 2, 3, 4, 5, 6]'''


def num_():
    l = [[1, 2], [3, 4], [5, 6]]
    x = [j for i in l for j in i]
    print(x)


def he_bing():
    a = [1, 5, 7, 9]
    b = [2, 2, 6, 8]
    # a.extend(b)
    n = a + b
    print(a)
    print(n)


'''如何打乱一个列表的元素'''


def distri():
    import random
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print(a)


def paixu():
    d1 = [
        {'name': 'alice', 'age': 38},
        {'name': 'bob', 'age': 18},
        {'name': 'Carl', 'age': 28},
    ]
    print(sorted(d1, key=lambda x: x["age"]))
    d = {'a': '1', 'b': '2'}
    print({v: k for k, v in d.items()})


def x():
    a = ("a", "b")
    b = (1, 2)
    print(zip(a, b))
    print(dict(zip(a, b)))


def shengchengqi():
    from itertools import islice
    gen = iter(range(10))  # iter()函数用来生成迭代器
    # 第一个参数是迭代器，第二个参数起始索引，第三个参数结束索引，不支持负数索引
    for i in islice(gen, 0, 4):
        print(i)


if __name__ == '__main__':
    shengchengqi()
