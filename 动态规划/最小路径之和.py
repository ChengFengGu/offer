class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            dp[i][0] = sum([grid[k][0] for k in range(0, i)]) + grid[i][0]
        for j in range(n):
            dp[0][j] = sum([grid[0][k] for k in range(0, j)]) + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()

    result = s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    # result = s.minPathSum([[1, 3], [1, 5]])

    print(result)
