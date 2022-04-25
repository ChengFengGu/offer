# @algorithm @lc id=144 lang=python3
# @title binary-tree-preorder-traversal


from cn.Python3.mod.preImport import *


# @test([1,null,2,3])=[1,2,3]
# @test([])=[]
# @test([1])=[1]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        results = []
        
        if root == None:
            return results
        stack.append(root)
        while len(stack) > 0:
            
            curr:TreeNode = stack.pop()
            results.append(curr.val)
            
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
                
        return results
        
        
        
