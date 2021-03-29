if __name__ == '__main__':
    for i in range(10):
        print("* " * (i + 1))
    print('_________________________')
    for i in range(10):
        print('* ' * (10 - i))
    print('_________________________')
    for i in range(10):
        print(' ' * (10 - i) + '* ' * (i + 1))
    for i in range(10):
        print(' ' * (i + 1) + '* ' * (10 - i))
