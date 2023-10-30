"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9


提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n

        stack = []
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    left[i] = i
                else:
                    left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    right[i] = n - 1
                else:
                    right[i] = stack[-1]
            stack.append(i)

        water = 0
        for i in range(n):
            water += min(height[right[i]], height[left[i]]) - height[i]
        return water
