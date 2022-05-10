// @algorithm @lc id=66 lang=java 
// @title plus-one

package _66_Plus_One;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// @test([1,2,3])=[1,2,4]
// @test([4,3,2,1])=[4,3,2,2]
// @test([9])=[1,0]
public class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i] ++;
            if (digits[i] == 10){
                digits[i] = 0;
            }else{
                return digits;
            }
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}