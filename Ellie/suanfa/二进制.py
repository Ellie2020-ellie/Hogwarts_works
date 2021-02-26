"""
二进制加法
"""


def binary_add(a: str, b: str):
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    num1 = input("输入第一个数，二进制格式:\n")
    num2 = input("输入第二个数，二进制格式:\n")
    print(binary_add(num1, num2))
