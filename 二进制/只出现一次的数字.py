class Solution:
    def singleNumber(self, nums:list) -> int:
        ans = 0
        for i in range(32):
            total = sum((num>>i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1<<i)
                else:
                    ans |= (1<<i)

if __name__ == "__main__":
    s = Solution()
    result = s.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])
    print(result)