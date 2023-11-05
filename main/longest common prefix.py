"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcp_left = lcp(start, mid)
            lcp_right = lcp(mid + 1, end)
            min_len = min(len(lcp_left), len(lcp_right))
            for i in range(min_len):
                if lcp_left[i] != lcp_right[i]:
                    return lcp_left[:i]
            return lcp_left[:min_len]

        return lcp(0, len(strs) - 1)
