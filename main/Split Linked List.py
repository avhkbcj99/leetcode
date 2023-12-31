"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。



示例 1：


输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]


提示：

链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = ListNode()
        small_cur = small_head
        large_head = ListNode()
        large_cur = large_head
        cur = head
        while cur:
            if cur.val < x:
                small_cur.next = cur
                small_cur = small_cur.next
            else:
                large_cur.next = cur
                large_cur = large_cur.next
            cur = cur.next
        small_cur.next = large_head.next
        large_cur.next = None
        return small_head.next
