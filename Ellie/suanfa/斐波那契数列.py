def fibonacci(num):
    a, b = 0, 1
    l = [a, b]
    for i in range(num):
        a, b = b, a + b
        l.append(b)
    return l


if __name__ == '__main__':
    print(fibonacci(10))
