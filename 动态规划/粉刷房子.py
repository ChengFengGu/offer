# ====================================================

# 题目：一排n幢房子要粉刷成红色、绿色和蓝色，不同房子被粉刷成不同颜色的成本不同。用一个n×3的数组表示n幢房子分别用3种颜色粉刷的成本。要求任意相邻的两幢房子的颜色都不一样，请计算粉刷这n幢房子的最少成本。例如，粉刷3幢房子的成本分别为[[17，2，16]，[15，14，5]，[13，3，1]]，如果分别将这3幢房子粉刷成绿色、蓝色和绿色，那么粉刷的成本是10，是最少的成本。

# ====================================================

# ====================================================
# 状态转移方程: r(i) = min(g(i-1),b(i-1)) + cost[i][0]
#             g(i) = min(r(i-1),b(i-1)) + cost[i][1]
#             b(i) = min(r(i-1),g(i-1)) + cost[i][2]
# ====================================================


# ====================================================
# 递归版本 带缓存
# ====================================================
def helper(cost:list,i:int,n:int,r:list,g:list,b:list,dp:list):
    
    if i == 0:
        dp[i] = min(cost[i])
        r[i] = cost[i][0]
        g[i] = cost[i][1]
        b[i] = cost[i][2]
    elif i < n:
        if dp[i] == -1:
            
        
    
    pass



def lowest_cost(cost: list):
    n = len(cost)
    dp = [-1 for _ in range(n)]
    r = [-1 for _ in range(n)]
    g = [-1 for _ in range(n)]
    b = [-1 for _ in range(n)]

    for i in range(n):
        if i == 0:
            dp[i] = min(cost[i])
            r[i] = cost[i][0]
            g[i] = cost[i][1]
            b[i] = cost[i][2]
        else:
            r[i] = min(g[i - 1], b[i - 1]) + cost[i][0]
            g[i] = min(r[i - 1], b[i - 1]) + cost[i][1]
            b[i] = min(r[i - 1], g[i - 1]) + cost[i][2]

        dp[i] = min(r[i], g[i], b[i])
    return dp[n-1]


if __name__ == "__main__":
    result = lowest_cost([[17, 2, 16], [15, 14, 5], [13, 3, 1]])
    print(result)
