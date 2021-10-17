'''
Author: your name
Date: 2021-10-17 15:12:25
LastEditTime: 2021-10-17 15:16:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /offer/在二叉树中找到两个节点的最近公共祖先.py
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self , root:TreeNode , o1 , o2 ):
        # write code here
        # 用什么遍历？ 中序，遍历完成之后，两者的中间节点进行筛选
        # 再进行层次遍历，如果该节点所在的层，
        
        