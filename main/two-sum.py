def two_sum(nums, target):
    # 创建一个字典，用于存储数字和它们的索引
    num_to_index = {}

    for index, num in enumerate(nums):
        # 计算当前数字的补数
        complement = target - num

        # 如果补数在字典中，返回它们的索引
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # 否则，将当前数字及其索引添加到字典中
        num_to_index[num] = index

    # 如果没有找到匹配的组合，返回一个空列表或其他适当的标志
    return []
