import math


class Solution:
    def minimumTotal(self, triangle: list) -> int:
        if len(triangle) == 0:
            return 0

        width = max([len(line) for line in triangle])
        dp = [[math.inf for _ in range(width)] for i in range(len(triangle))]

        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):  # j代表层数
            for j in range(0, len(triangle[i])):  #
                if j == 0:
                    dp[i][j] = min(dp[i][0], dp[i][1]) + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + triangle[i][j]
        return min(dp[len(triangle) - 1])


if __name__ == "__main__":
    s = Solution()
    result = s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(result)
