def merge(nums1, m, nums2, n):
    # 初始化两个指针，分别指向nums1和nums2的末尾
    p1 = m - 1
    p2 = n - 1
    # 初始化合并后的数组的末尾指针
    p = m + n - 1

    # 从后向前合并两个数组
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # 如果nums2中还有元素未合并，将其复制到nums1中
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
