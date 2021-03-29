"""
单链表反转
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SingleLinkList:
    def __init__(self, head=None):
        """链表的头部"""
        self._head = head

    def add(self, val: int):
        """
        给链表添加元素
        :param val: 传过来的数字
        :return:
            """
        # 创建一个节点
        node = Node(val)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next  # 移动游标
                # 退出循环的时候，cur指向的尾结点
                cur.next = node


    def traversal(self):
        if self._head is None:
            return
        else:
            cur = self._head
            while cur is not None:
                print(cur.val)
            cur = cur.next


    def size(self):
        """
        获取链表的大小
        :return:
        """
        count = 0
        if self._head is None:
            return count
        else:
            cur = self._head
            while cur is not None:
                count += 1
            cur = cur.next
            return count


    def reverse(self):
        """
        单链表反转
        思路:
        让 cur.next 先断开即指向 none，指向设定 pre 游标指向断开的元素，然后
        cur.next 指向断开的元素，再把开始 self._head 再最后一个元素的时候.
        :return:
        """
        if self._head is None or self.size() == 1:
            return
        else:
            pre = None
            cur = self._head
            while cur is not None:
                post = cur.next
                cur.next = pre
                pre = cur
                cur = post
                self._head = pre  # 逆向后的头节点


if __name__ == '__main__':
    single_link = SingleLinkList()
    single_link.add(3)
    single_link.add(5)
    single_link.add(6)
    single_link.add(7)
    single_link.add(8)
    # print("对链表进行遍历")
    # single_link.traversal()
    # print(f"size:{single_link.size()}")
    # print("对链表进行逆向操作之后")
    # single_link.reverse()
    # single_link.traversal()
