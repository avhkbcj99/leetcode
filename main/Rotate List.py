"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]


提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
        # def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #     if not head:
        #         return head
        #     cur = head
        #     length = 0
        #     while cur:
        #         cur = cur.next
        #         length += 1
        #     k = k % length
        #     if k == 0:
        #         return head
        #     slow, fast = head, head
        #     for _ in range(k):
        #         fast = fast.next
        #     while fast.next:
        #         slow = slow.next
        #         fast = fast.next
        #     new_head = slow.next
        #     slow.next = None
        #     fast.next = head
        #     return new_head

        def rotateRight(self, head: ListNode, k: int) -> ListNode:
            if not head:
                return head
            cur = head
            length = 0
            while cur:
                cur = cur.next
                length += 1
            k = k % length
            if k == 0:
                return head
            slow, fast = head, head
            for _ in range(k):
                fast = fast.next
            while fast.next:
                slow = slow.next
                fast = fast.next
            new_head = slow.next
            slow.next = None
            fast.next = head
            return new_head
