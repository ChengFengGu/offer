#  题目：输入3个字符串s1、s2和s3，请判断字符串s3能不能由字符串s1和s2交织而成，即字符串s3的所有字符都是字符串s1或s2中的字符，字符串s1和s2中的字符都将出现在字符串s3中且相对位置不变。例如，字符串"aadbbcbcac"可以由字符串"aabcc"和"dbbca"交织而成，如图14.5所示。

# https://weread.qq.com/web/reader/4e132bc07263ff664e11075k09332a2023b093f65e0888c


    class Solution:
        def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

            if len(s1) + len(s2) != len(s3):
                return False
            dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
            dp[0][0] = True

            for i in range(len(s1)):
                dp[i + 1][0] = s1[i] == s3[i] and dp[i][0]
            for j in range(len(s2)):
                dp[0][j + 1] = s2[j] == s3[j] and dp[0][j]
            for i in range(len(s1)):
                for j in range(len(s2)):
                    ch1 = s1[i]
                    ch2 = s2[j]
                    ch3 = s3[i + j + 1]
                    dp[i + 1][j + 1] = (ch1 == ch3 and dp[i][j + 1]) or (
                        ch2 == ch3 and dp[i + 1][j]
                    )
            return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("", "", ""))
