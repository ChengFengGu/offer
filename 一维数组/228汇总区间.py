class Solution:
    def summaryRanges(self, nums: list) -> list:
        n = len(nums)
        result = []
        low = 0
        for i in range(1,n):
            if nums[i] - nums[i-1]  > 1:
                if low == i-1:
                    result.append(f"{nums[i-1]}")
                else:
                    result.append(f"{nums[low]}->{nums[i-1]}")
                low = i
            
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.summaryRanges([0,1,2,4,5,7])
    print(result)