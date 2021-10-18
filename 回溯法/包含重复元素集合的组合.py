def helper(nums: list, k: int, index: int, subset: list, result: list):
    if k == 0:
        result.append(sorted(subset.copy()))
    elif index < len(nums):
        helper(nums, k, index + 1, subset, result)
        subset.append(nums[index])
        helper(nums, k, index + 1, subset, result)
        subset.pop()


def subsets(nums: list, k: int):

    subset = []
    result = []

    helper(nums, k, 0, subset, result)

    return result

    print(result)


if __name__ == "__main__":
    subsets([2, 2, 2, 4, 3, 3], 8)
