"""
Author: your name
Date: 2021-10-17 15:12:25
LastEditTime: 2021-10-17 15:25:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /offer/在二叉树中找到两个节点的最近公共祖先.py
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mid_traveller(self, node: TreeNode, layer, container: list):
        container.append((node.val, layer))

        if node.left != None:
            return self.mid_traveller(node.left, layer + 1, container)
        if node.right != None:
            return self.mid_traveller(node.right, layer + 1, container)
        else:
            return container

    def lowestCommonAncestor(self, root: TreeNode, o1, o2):
        # write code here
        # 用什么遍历？ 中序，遍历完成之后，两者的中间节点进行筛选
        # 再进行层次遍历，找到这些中间节点共同所在的层，先用n-1层的节点，判断是否两个子树中包含这两个节点；之后再n-2层的节点。 对就这样

        mid_traveller_list = self.mid_traveller(root, 0, [])

        idx = 0
        for val, layer in mid_traveller_list:
            if val == o1:
                index1 = idx
                layer1 = layer
            if val == o2:
                index2 = idx
                layer2 = layer
            idx += 1

        index1 = mid_traveller_list.index(o1)
        index2 = mid_traveller_list.index(o2)

        cand_nodes = mid_traveller_list[index1 + 1, index2]
        filter_nodes = []
        for val, layer in cand_nodes:
            if layer < min(layer1, layer2):
                if mid_traveller_list.index((val, layer)) < max(
                    index1, index2
                ) and mid_traveller_list.index((val, layer)) > min(index1, index2):
                    filter_nodes.append(val, layer)

        layer = min(layer1, layer2)
        layer_dist = min(layer1, layer2) - 0
        for v,l in filter_nodes:
            if l < 
