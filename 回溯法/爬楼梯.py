def helper(cost: list, index: int):
    if index <= 2:
        return cost[index]
    else:
        return min(helper(cost, index - 1), helper(cost, index - 2)) + cost[index]


def mincost(cost: list):
    result = helper(cost, 0)
    return result


if __name__ == "__main__":
    print(mincost([3, 5, 3,1,7]))
