def helper(nums: list, k: int, index: int, subset: list, result: list):
    if k == 0:
        result.append(subset.copy())

    elif k > 0 and index < len(nums):

        helper(nums, k, index + 1, subset, result)
        subset.append(nums[index])
        helper(nums, k - nums[index], index, subset, result)
        subset.pop()


def subsets(nums: list, k: int):
    subset = []
    result = []
    helper(nums, k, 0, subset, result)
    return result


if __name__ == "__main__":
    print(subsets([2, 3, 5], 8))
