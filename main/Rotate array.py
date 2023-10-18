# 解法一
def rotate(nums, k):
    n = len(nums)
    k = k % n  # 确保k在数组长度范围内

    # 使用切片操作将数组分成两部分，然后交换它们的位置
    nums[:k], nums[k:] = nums[n - k:], nums[:n - k]


# 示例 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)  # 输出: [5, 6, 7, 1, 2, 3, 4]

# 示例 2
nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print(nums2)  # 输出: [3, 99, -1, -100]


# 解法二
def rotate(nums, k):
    n = len(nums)
    k = k % n  # 确保k在数组长度范围内

    # 先将整个数组反转
    reverse(nums, 0, n - 1)
    # 然后将前k个元素反转
    reverse(nums, 0, k - 1)
    # 最后将剩余的元素反转
    reverse(nums, k, n - 1)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


# 示例 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print(nums1)  # 输出: [5, 6, 7, 1, 2, 3, 4]

# 示例 2
nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print(nums2)  # 输出: [3, 99, -1, -100]
