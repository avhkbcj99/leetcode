"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。



示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false


提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100


进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def dfs(left, right):
    #         if not left and not right:
    #             return True
    #         if not left or not right:
    #             return False
    #         if left.val != right.val:
    #             return False
    #         return dfs(left.left, right.right) and dfs(left.right, right.left)
    #
    #     return dfs(root.left, root.right) if root else True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
