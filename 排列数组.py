def judge(s:str,t:str,swaps:list,k:int):
    for i in range(len(s)):
        if s[i] != t[i]


if __name__ == '__main__':
    line = input()
    T = int(line)

    
    for i in range(T):
        line = input()
        k,n = tuple([int(e) for e in line.split()])
        
        swaps = []
        for j in range(n):
            swaps.append(input())
        s = input()
        t = input()

        