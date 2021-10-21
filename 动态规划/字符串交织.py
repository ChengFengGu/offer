#  题目：输入3个字符串s1、s2和s3，请判断字符串s3能不能由字符串s1和s2交织而成，即字符串s3的所有字符都是字符串s1或s2中的字符，字符串s1和s2中的字符都将出现在字符串s3中且相对位置不变。例如，字符串"aadbbcbcac"可以由字符串"aabcc"和"dbbca"交织而成，如图14.5所示。

# https://weread.qq.com/web/reader/4e132bc07263ff664e11075k09332a2023b093f65e0888c


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2))] for _ in range(len(s1))]
        dp[0][0] = True

        for 

if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("abc", "def", "abcdef"))
