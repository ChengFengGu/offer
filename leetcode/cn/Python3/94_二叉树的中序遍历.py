# @algorithm @lc id=94 lang=python3
# @title binary-tree-inorder-traversal


from cn.Python3.mod.preImport import *

# @test([1,2])=[2,1]
# @test([1,2,3])=[2,1,3]
# @test([1,2,4,null,3])=[4,2,1,3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        results = []
        stack = []
        if root == None:
            return []
        
        curr:TreeNode = root
        while curr.left

        return results

