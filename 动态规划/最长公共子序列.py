#%%

# 题目：输入两个字符串，请求出它们的最长公共子序列的长度。如果从字符串s1中删除若干字符之后能得到字符串s2，那么字符串s2就是字符串s1的一个子序列。例如，从字符串"abcde"中删除两个字符之后能得到字符串"ace"，因此字符串"ace"是字符串"abcde"的一个子序列。但字符串"aec"不是字符串"abcde"的子序列。如果输入字符串"abcde"和"badfe"，那么它们的最长公共子序列是"bde"，因此输出3。


#%%


def longest_sub_array(s1: str, s2: str):

    dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

    for i in range(len(s1)):
        for j in range(len(s2)):
            if i == 0 or j == 0:
                dp[i, j] = 1  # 空字符串作为最长公共子序列
            else:
                if s1[i] == s2[j]:
                    dp[i, j] = dp[i - 1, j - 1] + 1
                else:
                    dp[i, j] = max(dp[i - 1, j], dp[i, j - 1])
    return dp[len(s1) - 1, len(s2) - 1]


if __name__ == "__main__":

    print(longest_sub_array("abd", "abe"))

# %%
