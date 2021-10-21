#  题目：输入3个字符串s1、s2和s3，请判断字符串s3能不能由字符串s1和s2交织而成，即字符串s3的所有字符都是字符串s1或s2中的字符，字符串s1和s2中的字符都将出现在字符串s3中且相对位置不变。例如，字符串"aadbbcbcac"可以由字符串"aabcc"和"dbbca"交织而成，如图14.5所示。

# https://weread.qq.com/web/reader/4e132bc07263ff664e11075k09332a2023b093f65e0888c


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True

        if len(s1) == 0:
            return True if s2 == s3 else False
        if len(s2) == 0:
            return True if s1 == s3 else False

        dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

        for i in range(len(s1)):
            for j in range(len(s2)):
                if i == 0:
                    

if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("abc", "def", "abcdef"))
