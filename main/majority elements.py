def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate


# 示例用法
nums = [3, 2, 3]
result = majority_element(nums)
print(result)  # 输出 3
