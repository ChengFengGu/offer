'''
Author: your name
Date: 2021-10-17 16:36:00
LastEditTime: 2021-10-17 16:38:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /offer/表达式求值.py
'''
class Solution:
    def solve(self , s ):
        # write code here
        # 符号栈 数字栈 计算优先级 括号>乘>加=减
        # 符号栈： 规则： 遇到一半括号，则等待另一个括号再进行计算，