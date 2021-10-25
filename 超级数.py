
if __name__ == '__main__':
    line = input()
    n,k = tuple([int(e) for e in line.split()])

    line = input()
    nums = [int(e) for e in line.split()]

    
    while len(nums) >= k:
        nums.remove(nums.index(max(nums[:k+1])))
    print(nums)
