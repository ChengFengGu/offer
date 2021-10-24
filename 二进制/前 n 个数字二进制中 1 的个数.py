class Solution:
    def countBits(self, n: int):
        result = [0 for _ in range(n+1)]
        for i in range(n+1):
            j = i
            while j!=0:
                result[i] += 1
                j = j & (j-1)
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.countBits(6)
    print(result)
