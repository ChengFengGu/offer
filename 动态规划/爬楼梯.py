# def helper(cost: list, index: int):
#     if index <= 2:
#         return cost[index]
#     else:
#         return min(helper(cost, index - 1), helper(cost, index - 2)) + cost[index]

# 百度校招笔试题,#TODO
def helper(cost: list, i: int, dp: list):
    if i < 2:
        dp[i] = cost[i]
    elif dp[i] == 0:
        helper(cost, i - 2, dp)
        helper(cost, i - 1, dp)
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]


def mincost(cost: list):
    dp = [0 for i in range(len(cost))]
    helper(cost, len(cost) - 1, dp)
    return min(dp[len(cost) - 2], dp[len(cost) - 1])


def mincost_v2(cost: list):
    dp = [0 for _ in range(len(cost))]
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    return min(dp[len(cost) - 2], dp[len(cost) - 1])


def mincost_v3(cost: list):
    dp = [cost[0], cost[1]]
    for i in range(2, len(cost)):
        dp[i % 2] = min(dp[0], dp[1]) + cost[i]

    return min(dp[0], dp[1])


if __name__ == "__main__":
    print(mincost_v3([7, 3, 5, 5, 5]))
