# @algorithm @lc id=92 lang=python3
# @title reverse-linked-list-ii


from cn.Python3.mod.preImport import *

# @test([1,2,3,4,5],2,4)=[1,4,3,2,5]
# @test([5],1,1)=[5]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        idx = 1
        prev = None
        curr = head

        while curr != None:
            if idx >= left and idx <= right:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                
            else:
                curr = curr.next
                prev = curr

            idx += 1

        return prev
