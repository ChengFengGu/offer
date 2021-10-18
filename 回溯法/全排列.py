# 题目：给定一个没有重复数字的集合，请找出它的所有全排列。例如，集合[1，2，3]有6个全排列，分别是[1，2，3]、[1，3，2]、[2，1，3]、[2，3，1]、[3，1，2]和[3，2，1]

def helper(nums:int,index:int,set:list,result:list):

    if len(set) == len(nums):
        result.append(set.copy())
    elif index < len(nums):
        helper(nums,index+1,set,result)
        set.append(nums[index])
        helper(nums,index+1,set,result)
        set.pop()


def sets(nums:list):
    set = []
    result = []
    helper(nums,0,set,result)
    return result

if __name__ == '__main__':
    print(sets([1,2,3]))