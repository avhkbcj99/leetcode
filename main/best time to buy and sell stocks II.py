def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    buy = [0] * n
    sell = [0] * n

    buy[0] = -prices[0]
    sell[0] = 0

    for i in range(1, n):
        if i == 1:
            buy[i] = max(buy[i - 1], -prices[i])
        else:
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
        sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

    return sell[-1]


# 示例测试
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))  # 输出: 7

prices2 = [1, 2, 3, 4, 5]
print(maxProfit(prices2))  # 输出: 4

prices3 = [7, 6, 4, 3, 1]
print(maxProfit(prices3))  # 输出: 0
