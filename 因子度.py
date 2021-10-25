import math

if __name__ == '__main__':
    line  =  input()
    n = int(line)

    line = input()
    nums = [int(e) for e in line.split()]

    dp = [0 for k in range(0,max(nums)+1)]
    dp[0] = None
    dp[1] = None
    
    n = len(nums)
    for k in range(2,max(nums)):
        for i in range(n):
            if nums[i] % k == 0:
                dp[k]

    