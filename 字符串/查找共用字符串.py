class Solution:
    def char2index(self,char:str):
        return ord(char)-ord('a')

    def commonChars(self, words: list) -> list:
        result = []
        minfreq = [0 for _ in range(26)]
        n = len(words)
        for char in words[0]:
            minfreq[self.char2index(char)] += 1
        for i in range(1,n):
            freq = [0 for _ in range(26)]
            for char in words[i]:
                freq[self.char2index(char)] += 1
            for j in range(26):
                minfreq[j] = min(minfreq[j],freq[j])
        for i in range(26):
            for j in range(0,minfreq[i]):
                result.append(chr(i+ord('a')))
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.commonChars(["bella","label","roller"])
    print(result)