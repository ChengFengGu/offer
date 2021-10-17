"""
Author: your name
Date: 2021-10-17 16:36:00
LastEditTime: 2021-10-17 16:44:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /offer/表达式求值.py
"""


class Solution:
    def solve(self, s):
        # write code here
        # 符号栈 数字栈 计算优先级 括号>乘>加=减
        # 符号栈： 规则： 遇到一半括号，则等待另一个括号再进行计算
        # 数字符号全入栈，遇加减等待，遇乘法等待，遇一半括号，则等待另一个括号再进行计算
        ops = []
        nums = []

        for char in s:
            if char in ["+", "-", "*", "(", ")"]:
                ops.append(char)
            if char in ["{i}" for i in range(0, 9)]:
                nums.append(char)

        # compute
        temp = 0 # 当前表达式的值
        while ops.pop() != None:
            