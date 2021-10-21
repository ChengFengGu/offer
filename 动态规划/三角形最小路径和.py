class Solution:
    def minimumTotal(self, triangle:list) -> int:
        if len(triangle) == 0:
            return 0
        dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]

        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):  # j代表层数
            for j in range(1, len(triangle[i])):  #
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[len(triangle) - 1])


if __name__ == "__main__":
    s = Solution()
    result = s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(result)
