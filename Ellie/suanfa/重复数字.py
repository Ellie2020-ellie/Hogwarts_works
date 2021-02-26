"""
从头扫到尾，只要当前元素值与下标不同，就做一次判断,numbers[i]与 numbers[numbers[i]]，
相等就认为找到了重复元素，返回 true,否则就交换两者，继续循环。直到最后还没找到认为没找到重复元素。

"""


# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers):
        if numbers is None or len(numbers) <= 1:
            return False
        use_set = set()
        duplication = {}
        for index, value in enumerate(numbers):
            if value not in use_set:
                use_set.add(value)
            else:
                duplication[index] = value
        return duplication


if __name__ == '__main__':
    s = Solution()
    d = s.duplicate([1, 2, -3, 4, 4, 95, 95, 5, 2, 2, -3, 7, 7, 5])
    print(d)
