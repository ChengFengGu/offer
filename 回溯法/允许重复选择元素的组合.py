


def helper(nums: list, k: int, index: int, subset: list, result: list):
    if sum(subset) == k:
        result.append(subset.copy())
    elif index < len(nums):
        subset.append(nums[index])


def subsets(nums: list, k: int):
    pass
