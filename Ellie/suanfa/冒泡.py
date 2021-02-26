'''冒泡排序算法的原理如下：

1，比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2，对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
3，针对所有的元素重复以上的步骤，除了最后一个。

4，持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def maopao(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
    maopao(l)
    print(l)
