'''快速排序的概念很简单就是把序列分成三部分。
一个中点，中点的左边都比中点“小”，右边都比中shu点“大”
然后再分别对左右两边进行相同的处理。
可以想象这样会把序列不断切分。而当序列小于三个元素的时候，这么处理的结果就是从小到大排列。'''


def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        # mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素
        mid = data[0]
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


# 示例：
array = [17, 18, 2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
y = quick_sort(array)
print(y)
# x = sorted(quick_sort(array))
print(y[::-1])


# 输出为[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9, 10, 12, 15, 15, 17]
def quick_sort(arr, first, last):
    if first >= last:
        return
    mid_value = arr[first]
    low = first
    high = last
    while low < high:
        while low < high and arr[high] >= mid_value:
            high -= 1  # 游标左移
            arr[low] = arr[high]

    while low < high and arr[low] < mid_value:
        low += 1
        arr[high] = arr[low]
        arr[low] = mid_value
    quick_sort(arr, first, low - 1)
    quick_sort(arr, low + 1, last)


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 55, 6, 3, 4, 5, 6]
    quick_sort(l, 0, len(l) - 1)
    print(l)
