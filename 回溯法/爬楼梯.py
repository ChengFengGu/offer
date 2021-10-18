def helper(cost: list, index: int):
    if index <= 2:
        return cost[index]
    else:
        return min(helper(cost, index - 1), helper(cost, index - 2)) + cost[index]


def mincost(cost: list):
    result = min(helper(cost, len(cost) - 1), helper(cost, len(cost) - 2))
    return result


if __name__ == "__main__":
    print(mincost([7,3,5,5,5]))
