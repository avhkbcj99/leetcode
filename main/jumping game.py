def canJump(nums):
    max_reach = 0  # 初始时能够到达的最远下标为0
    for i in range(len(nums)):
        # 如果当前下标超过了最远可到达的下标，返回False
        if i > max_reach:
            return False
        # 更新max_reach为当前下标和当前下标加上跳跃长度的最大值
        max_reach = max(max_reach, i + nums[i])
        # 如果max_reach达到或超过了最后一个下标，返回True
        if max_reach >= len(nums) - 1:
            return True
    return True


# 示例用法
nums1 = [2, 3, 1, 1, 4]
print(canJump(nums1))  # 输出True

nums2 = [3, 2, 1, 0, 4]
print(canJump(nums2))  # 输出False
