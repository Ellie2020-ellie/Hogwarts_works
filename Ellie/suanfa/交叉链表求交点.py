# Definition for singly-linked list.
'''cur1、cur2，2个指针的初始位置是链表headA、headB头结点，cur1、cur2两个指针一直往后遍历。 直到cur1指针走到链表的末尾，然后cur1指向headB；
直到cur2指针走到链表的末尾，然后cur2指向headA； 然后再继续遍历； 每次cur1、cur2指向None，则将cur1、cur2分别指向headB、headA。
循环的次数越多，cur1、cur2的距离越接近，直到cur1等于cur2。则是两个链表的相交点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):

        """
        :tye head1, head1: ListNode
        :rtye: ListNode
        """
        if headA is not None and headB is not None:
            cur1, cur2 = headA, headB

        while cur1 != cur2:
            cur1 = cur1.next if cur1 is not None else headA
            cur2 = cur2.next if cur2 is not None else headB

        return cur1
