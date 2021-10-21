class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        # s为空串的时候
        for j in range(len(t)):
            if j == 0:
                dp[0][j] = 1
            else:
                dp[0][j] = 0

        # t为空串的时候
        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]
                dp[i+1][j+1] = dp[i][j] + dp[i][j+1]


if __name__ == "__main__":
    s = Solution()
    result = s.numDistinct("rabbbit", "rabbit")
    print(result)
