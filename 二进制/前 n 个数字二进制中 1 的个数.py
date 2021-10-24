class Solution:
    def countBits(self, n: int):
        result = [-1 for _ in range(n+1)]
        for i in range(n):
            j = i
            while j!=0:
                result[i] += 1
                j = j & (j-1)
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.countBits(2)
    print(result)
