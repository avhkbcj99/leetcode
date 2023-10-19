def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]  # 初始化买入价格为第一天的价格
    max_profit = 0  # 初始化最大利润为0

    for price in prices:
        if price < min_price:
            min_price = price  # 更新最低买入价格
        else:
            max_profit = max(max_profit, price - min_price)  # 更新最大利润

    return max_profit


# 示例用法
prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))  # 输出: 5

prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))  # 输出: 0
