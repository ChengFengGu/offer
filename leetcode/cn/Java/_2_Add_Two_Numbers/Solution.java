// @algorithm @lc id=2 lang=java 
// @title add-two-numbers

package _2_Add_Two_Numbers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.print.DocFlavor.INPUT_STREAM;

import algm.*;

// @test([2,4,3],[5,6,4])=[7,0,8]
// @test([0],[0])=[0]
// @test([9,9,9,9,9,9,9],[9,9,9,9])=[8,9,9,9,0,0,0,1]
// @test([2,4,9], [5,6,4,9])=[7,0,4,0,1] 
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        List<Integer> num1 = new ArrayList<>();
        List<Integer> num2 = new ArrayList<>();

        while (l1 != null) {
            num1.add(l1.val);
            l1 = l1.next;
        }
        Collections.reverse(num1);

        while (l2 != null) {
            num2.add(l2.val);
            l2 = l2.next;
        }
        Collections.reverse(num2);

        int p1 = num1.size() - 1;
        int p2 = num2.size() - 1;
        int carry = 0;

        List<Integer> res = new ArrayList<>();
        while (p1 >= 0 || p2 >= 0) {
            int x = p1 >= 0 ? num1.get(p1) : 0;
            int y = p2 >= 0 ? num2.get(p2) : 0;
            int sum = x + y + carry;
            res.add(sum % 10);
            carry = sum / 10;
            p1--;
            p2--;
        }
        if (carry != 0) {
            res.add(carry);
        }
        // Collections.reverse(res);
        ListNode resnode = new ListNode();
        ListNode resnode_p = resnode;

        for (int i = 0; i < res.size(); i++) {
            resnode.val = res.get(i);

            if (i != res.size()-1) {
                resnode.next = new ListNode();
                resnode = resnode.next;
            }

        }
        return resnode_p;
    }
}