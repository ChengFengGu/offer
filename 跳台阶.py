"""
Author: your name
Date: 2021-10-17 14:15:36
LastEditTime: 2021-10-17 14:15:37
LastEditors: your name
Description: In User Settings Edit
FilePath: /offer/跳台阶.py
"""

# https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=188&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fjob-code-high-week%2Fquestion-ranking

# -*- coding:utf-8 -*-

# https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=188&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fjob-code-high-week%2Fquestion-ranking
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return -1
        elif number == 1 or number == 2:
            return number
        else:
            return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(7))
