def find_single(l: list):
    result = 0
    for v in l:
        result ^= v
        if result == 0:
            print("没有落单元素")
        else:
            print("落单元素", result)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]
    find_single(l)
