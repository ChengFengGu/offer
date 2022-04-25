# @algorithm @lc id=145 lang=python3 
# @title binary-tree-postorder-traversal


from cn.Python3.mod.preImport import *
# @test([1,null,2,3])=[3,2,1]
# @test([])=[]
# @test([1])=[1]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        results = []
        def travel(root):
            if root == None:
                return
            if root.left != None:
                travel(root.left)
            if root.right != None:
                travel(root.right)
            if root != None:
                results.append(root.val)
        travel(root)
        return results