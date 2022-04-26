# @algorithm @lc id=1031 lang=python3 
# @title add-to-array-form-of-integer


from cn.Python3.mod.preImport import *
# @test([1,2,0,0],34)=[1,2,3,4]
# @test([2,7,4],181)=[4,5,5]
# @test([2,1,5],806)=[1,0,2,1]
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        