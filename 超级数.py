
if __name__ == '__main__':
    line = input()
    n,k = tuple([int(e) for e in line.split()])

    line = input()
    nums = [int(e) for e in line.split()]

    
    while len(nums) >= k:
        nums.remove(max(nums[:k+1]))
    for e in nums: print(e,end=' ')
