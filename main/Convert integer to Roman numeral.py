"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        1. 从大到小，依次判断
        2. 从左到右，依次判断
        """
        roman = ""
        while num > 0:
            if num >= 1000:
                roman += "M"
                num -= 1000
            elif num >= 900:
                roman += "CM"
                num -= 900
            elif num >= 500:
                roman += "D"
                num -= 500
            elif num >= 400:
                roman += "CD"
                num -= 400
            elif num >= 100:
                roman += "C"
                num -= 100
            elif num >= 90:
                roman += "XC"
                num -= 90
            elif num >= 50:
                roman += "L"
                num -= 50
            elif num >= 40:
                roman += "XL"
                num -= 40
            elif num >= 10:
                roman += "X"
                num -= 10
            elif num >= 9:
                roman += "IX"
                num -= 9
            elif num >= 5:
                roman += "V"
                num -= 5
            elif num >= 4:
                roman += "IV"
                num -= 4
            else:
                roman += "I"
                num -= 1
        return roman
