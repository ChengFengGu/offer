def helper(nums: list, k: int, index: int, subset: list, result: list):
    if k == 0:
        result.append(subset.copy())
    elif index < len(nums):
        helper(nums,k,index+1,subset,result)
        


def subsets(nums: list, k: int):
    pass
