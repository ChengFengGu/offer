def helper(nums: list, index: int, subset: list, result: list):
    if index == len(nums):
        result.append(subset.copy())
    elif index < len(nums):  # 有两个选择 是否将本字符串加入集合，分别选择加入和非加入，然后递归即可
        helper(nums, index + 1, subset, result)
        subset.append(nums[index])
        helper(nums, index + 1, subset, result)
        subset.pop()
    