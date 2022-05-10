# @algorithm @lc id=206 lang=python3 
# @title reverse-linked-list


from cn.Python3.mod.preImport import *
# @test([1,2,3,4,5])=[5,4,3,2,1]
# @test([1,2])=[2,1]
# @test([])=[]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev