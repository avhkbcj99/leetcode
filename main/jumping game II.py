def jump(nums):
    n = len(nums)
    max_reach = 0
    steps = 0
    current_position = 0

    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == current_position:
            steps += 1
            current_position = max_reach

    return steps


# 示例用法
nums1 = [2, 3, 1, 1, 4]
print(jump(nums1))  # 输出: 2

nums2 = [2, 3, 0, 1, 4]
print(jump(nums2))  # 输出: 2
