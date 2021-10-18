def helper(nums: list, k: int, index: int, subset: list, result: list):
    if k == 0:
        if sorted(subset.copy()) in result:
            pass
        else:
            result.append(sorted(subset.copy()))
    elif index < len(nums):
        helper(nums, k, index + 1, subset, result)
        subset.append(nums[index])
        helper(nums, k - nums[index], index + 1, subset, result)
        subset.pop()


def subsets(nums: list, k: int):

    subset = []
    result = []

    helper(nums, k, 0, subset, result)

    return sorted(result)


if __name__ == "__main__":
    print(subsets([2, 2, 2, 4, 3, 3], 8))
