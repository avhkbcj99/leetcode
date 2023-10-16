def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # 初始化唯一元素的数量为1，因为第一个元素一定是唯一的
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k
