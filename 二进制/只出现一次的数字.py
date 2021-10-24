class Solution:
    def singleNumber(self, nums:list) -> int:
        bitSums = [0 for _ in range(32)]
        # 所有数字的同一位置的数位相加。
        for num in nums:
            for i in range(0,32):
                bitSums[i] += (num >> (31-i)) & 1
        
        # 如果将出现3次的数字的
        result = 0
        for i in range(32):
            result = (result << 1) + bitSums[i]%3
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])
    print(result)