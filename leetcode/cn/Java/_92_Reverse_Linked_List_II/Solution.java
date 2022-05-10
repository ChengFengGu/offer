// @algorithm @lc id=92 lang=java 
// @title reverse-linked-list-ii

package _92_Reverse_Linked_List_II;

import javax.swing.event.ListDataEvent;

import algm.*;

// @test([1,2,3,4,5],2,4)=[1,4,3,2,5]
// @test([5],1,1)=[5]
// @test([3,5], 1, 2)=[5,3]
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
    public ListNode reverseBetween(ListNode head, int left, int right) {

        ListNode dummpyNode = new ListNode(-1);
        ListNode prev = dummpyNode;
        ListNode curr = curr;
        
        ListNode anchor1 = new ListNode();
        ListNode anchor2 = new ListNode();

        int idx = 1;
        while(curr!=null){
            if(idx==left){
                anchor1 = prev;
                anchor2 = curr;
            }
            if(idx>=left && idx <=right){
                ListNode next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
                if(idx==right){
                    anchor1.next = prev;
                    anchor2.next = curr;
                }
            }else{
                prev = curr;
                curr = curr.next;
            }
            
            idx += 1;
        }

        return prev;

    }
}