'''
Author: your name
Date: 2021-10-18 10:05:15
LastEditTime: 2021-10-18 10:05:15
LastEditors: your name
Description: In User Settings Edit
FilePath: /offer/所有子集.py
'''
"""
Author: your name
Date: 2021-10-18 09:59:38
LastEditTime: 2021-10-18 10:04:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /offer/所有子集.py
"""


def helper(nums: list, index: int, subset: list, result: list):
    if index == len(nums):
        result.append(subset)
    elif index < len(nums):
        result = helper(nums, index + 1, subset, result)
        
