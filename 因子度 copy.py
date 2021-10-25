import math

if __name__ == '__main__':
    line  =  input()
    n = int(line)

    line = input()
    nums = [int(e) for e in line.split()]

    dp = [0 for k in range(0,max(nums)+1)]
    dp[0] = -1
    dp[1] = -1
    
    n = len(nums)
    for i in range(n):
        pass

    print(dp.index(max(dp)))

    