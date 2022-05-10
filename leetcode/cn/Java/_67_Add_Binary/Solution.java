// @algorithm @lc id=67 lang=java 
// @title add-binary

package _67_Add_Binary;

// @test("11","1")="100"
// @test("1010","1011")="10101"
public class Solution {
    public String addBinary(String a, String b) {
        int l1 = a.length() - 1;
        int l2 = b.length() - 1;

        int carry = 0;

        StringBuffer res = new StringBuffer();
        while (l1 >= 0 || l2 >= 0) {
            int x = l1 >= 0 ? Integer.parseInt(String.valueOf(a.charAt(l1))) : 0;
            int y = l2 >= 0 ? Integer.parseInt(String.valueOf(b.charAt(l2))) : 0;
            int sum = x + y + carry;

            res.append((sum) % 2);

            carry = sum > 1 ? 1 : 0;
            l1--;
            l2--;
        }
        if (carry != 0) {
            res.append(carry);
        }
        return res.reverse().toString();
    }
}