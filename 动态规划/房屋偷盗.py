# %% [markdown]

# ### 题目：输入一个数组表示某条街道上的一排房屋内财产的数量。如果这条街道上相邻的两幢房屋被盗就会自动触发报警系统。请计算小偷在这条街道上最多能偷取到多少财产。例如，街道上5幢房屋内的财产用数组[2，3，4，5，3]表示，如果小偷到下标为0、2和4的房屋内盗窃，那么他能偷取到价值为9的财物，这是他在不触发报警系统的情况下能偷取到的最多的财物，如图14.3所示。被盗的房屋上方用特殊符号标出。

# ---

# 状态转移方程 : f(i) 为在进入第i个房屋之后能偷到的最多的财物。

# $f(i) = max(f(i-2)+nums[i],f(i-1) )$
# %%

# # v1  带缓存的递归代码
def helper(nums: list, i: int, dp: list):

    if i == 0:
        dp[i] = nums[i]
    elif i == 1:
        dp[1] == max(nums[1], nums[0])
    elif 

    elif i < len(nums) and i >= 2:
        helper(nums, i - 1, dp)
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])


def rob(nums: list):
    dp = [0 for i in range(len(nums))]
    length = len(nums)
    helper(nums, 0, dp)
    return max(dp[len - 1], dp[len - 2])


if __name__ == "__main__":
    rob([1, 2, 3, 4, 5])
