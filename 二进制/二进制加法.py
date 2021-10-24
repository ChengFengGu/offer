class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        str_result = ''
        i = len(a)-1
        j = len(b)-1

        carry = 0
        while (i>=0 or j >= 0):
            digitA = int(a[i]) if i>=0 else 0
            digitB = int(b[j]) if j>=0 else 0
            i -= 1
            j -= 1
            sum = digitA + digitB + carry
            carry = sum // 2
            result.append(sum%2)

        if carry == 1:
            result.append(1)

        for i in range(len(result)-1,-1,-1):
            str_result += str(result[i])
        return str_result

if __name__ == "__main__":
    s = Solution()
    result =  s.addBinary("1","1")
    print(result)