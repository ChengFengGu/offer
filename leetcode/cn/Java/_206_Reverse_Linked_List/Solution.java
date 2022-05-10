// @algorithm @lc id=206 lang=java 
// @title reverse-linked-list

package _206_Reverse_Linked_List;

import algm.*;

// @test([1,2,3,4,5])=[5,4,3,2,1]
// @test([1,2])=[2,1]
// @test([])=[]
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;

    }
}