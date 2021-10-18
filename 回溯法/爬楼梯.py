def helper(cost: list, index: int):
    if index <= 2:
        return cost[index]
    else:
        return min(helper(cost, index-1),helper(cost, index-2))

def mincost(cost: list):
    return helper(cost,0)


if __name__ == '__main__':
    print(mincost([1,2,3])