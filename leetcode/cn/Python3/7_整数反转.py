# @algorithm @lc id=7 lang=python3 
# @title reverse-integer


from cn.Python3.mod.preImport import *
# @test(123)=321
# @test(-123)=-321
# @test(120)=21
class Solution:
    def reverse(self, x: int) -> int:
        chars = list(str(x))
        left = 0
        right = len(chars)-1
        
        if not chars[0].isnumeric():
            left += 1
        while left < right:
            tmp = chars[left]
            chars[left] = chars[right]
            chars[right] = tmp
            
            left += 1
            right -= 1
        
        res = ''
        for item in chars:
            res += item
    
        res = int(res)
        # 处理溢出的情况
        if res > 2**31-1 or res < -2**31:
            return 0
        return res