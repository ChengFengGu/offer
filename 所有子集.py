


def helper(nums: list, index: int, subset: list, result: list):
    if index == len(nums):
        result.append(subset)
    elif index < len(nums):
        helper(nums, index + 1, subset, result)
        subset.append(nums[index])

        helper(nums, index + 1, subset, result)
