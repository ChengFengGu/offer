def helper(nums: list, index: int, subset: list, result: list):
    if index == len(nums):
        result.append(subset.copy())
    elif index < len(nums):  # 有两个选择 是否将本字符串加入集合，分别选择加入和非加入，然后递归即可
        helper(nums, index + 1, subset, result)
        subset.append(nums[index])
        helper(nums, index + 1, subset, result)
        subset.pop()  # 在回溯到父节点之前，应该清除已经对子集状态进行的修改。此前在子集subset中添加了一个数字，此时应该将它删除。


def subsets(nums: list):
    result = []
    if len(nums) == 0:
        return result
    subset = []
    result = []
    helper(nums, 0, subset, result)
    return result


if __name__ == "__main__":
    print(subsets([1,2,3]))