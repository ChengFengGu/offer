// @algorithm @lc id=415 lang=java 
// @title add-strings

package _415_Add_Strings;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

// @test("11","123")="134"
// @test("456","77")="533"
// @test("0","0")="0"
public class Solution {
    public String addStrings(String num1, String num2) {

        int l1 = num1.length() - 1;
        int l2 = num2.length() - 1;

        int carry = 0;

        StringBuffer res = new StringBuffer();

        while (l1 >= 0 || l2 >= 0) {
            int x = l1 >= 0 ? Integer.parseInt(String.valueOf(num1.charAt(l1))) : 0;
            int y = l2 >= 0 ? Integer.parseInt(String.valueOf(num2.charAt(l2))) : 0;
            int sum = x + y + carry;
            res.append(sum%10);
            carry = sum / 10;
            l1--;
            l2--;
        }
        if (carry != 0) {
            res.append(carry);
        }

        return res.reverse().toString();
        

    }
}