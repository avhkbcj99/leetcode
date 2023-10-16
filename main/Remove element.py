def remove_element(nums, val):
    # 初始化一个指针i，指向当前处理的元素位置
    i = 0
    # 遍历整个数组
    for j in range(len(nums)):
        # 如果当前元素不等于val，将其赋值给nums[i]
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    # 返回新长度i，即不包含val元素的数组长度
    return i


if __name__ == '__main__':
    # 示例用法
    lists = [3, 2, 2, 3, 4, 5, 2, 6]
    value = 2
    new_length = remove_element(lists, value)
    print(new_length)  # 输出新的数组长度，不包含值为2的元素
    print(lists[:new_length])  # 输出修改后的数组内容
