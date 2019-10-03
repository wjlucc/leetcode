def quick_sort(nums, left, right):
    if left < right and left >= 0 and right < len(nums):
        q = partition(nums, left, right)
        quick_sort(nums, left, q - 1)
        quick_sort(nums, q + 1, right)


def partition(nums, left, right):
    # 两个指针，一个标识当前小于判断值的位置，另一个标识数组元素
    min_index = left - 1
    judge_x = nums[right]
    for i in range(left, right + 1):
        if nums[i] <= judge_x:
            min_index += 1
            nums[min_index], nums[i] = nums[i], nums[min_index]
    return min_index


l = [2, 14, 1, 9, 7, 5, 8, 0, 32, 59, 11, 1, -2]
# l = [8, 9, 7, 5, 14]
print(l)
quick_sort(l, 0, len(l) - 1)
print(l)