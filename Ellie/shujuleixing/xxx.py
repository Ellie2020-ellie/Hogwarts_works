class Singleton(type):
    def __init__(self, *args, **kwargs):
        print("in __init__")
        self.__instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("in __call__")
        if self.__instance is None:
            self.__instance = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instance


class Foo(metaclass=Singleton):
    pass  # 在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在 Foo 实例化的时候执行。且仅会执行一次。


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


def post():
    print("this is post")
    print("想不到吧")


class Http():
    @classmethod
    def get(self):
        print("this is get ere")


def main():
    Http.get = post  # 动态的修改了 get 原因的功能，


if __name__ == '__main__':
    main()
    Http.get()
