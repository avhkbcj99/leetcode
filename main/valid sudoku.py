"""
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）


注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. 检查行
        for row in board:
            if not self.isValidList(row):
                return False
        # 2. 检查列
        for col in zip(*board):
            if not self.isValidList(col):
                return False
        # 3. 检查3*3的方格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValidList(square):
                    return False
        return True

    def isValidList(self, xs):
        xs = [x for x in xs if x != '.']
        return len(set(xs)) == len(xs)
