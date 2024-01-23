"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。



示例 1:


输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]
示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, postorder):
            if not inorder or not postorder:
                return None
            root = TreeNode(postorder[-1])
            idx = inorder.index(postorder[-1])
            root.left = build(inorder[:idx], postorder[:idx])
            root.right = build(inorder[idx + 1:], postorder[idx:-1])
            return root

        return build(inorder, postorder)
