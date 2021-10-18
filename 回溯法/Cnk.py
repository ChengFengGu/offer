def helper(n: int, k: int, index: int, combination: list, result: list):
    if len(combination) == k:
        result.append(combination.copy())
    elif index <= n:
        helper(n,k,index+1,combination,result)
        combination.append(index)
        helper(n,k,index+1,combination,result)
        combination.pop()

def subsets(n,k):
    result = []
    combination = []
    helper(n,k,)
