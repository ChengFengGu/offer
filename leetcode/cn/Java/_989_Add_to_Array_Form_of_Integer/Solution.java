// @algorithm @lc id=1031 lang=java 
// @title add-to-array-form-of-integer

package _989_Add_to_Array_Form_of_Integer;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// @test([1,2,0,0],34)=[1,2,3,4]
// @test([2,7,4],181)=[4,5,5]
// @test([2,1,5],806)=[1,0,2,1]
// @test([9,9,9,9,9,9,9,9,9,9], 1)=[1,0,0,0,0,0,0,0,0,0,0]
public class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> res = new ArrayList<>();

        int carry = 0;
        int i = num.length - 1;
        while (i >= 0 || k != 0) {
            int x = i >= 0 ? num[i] : 0;
            int y = k == 0 ? 0 : k % 10;
            int sum = x + y + carry;
            res.add((x + y + carry) % 10);

            i--;
            carry = sum / 10;
            k = k / 10;
        }
        if (carry != 0)
            res.add(carry);
        Collections.reverse(res);

        return res;
    }
}