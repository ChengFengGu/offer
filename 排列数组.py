def judge(s: str, t: str, swaps: list, k: int):
    for i in range(len(s) - 1):
        if s[i] != t[i] and s[i + 1] != t[i + 1]:
            if t[i] + t[i + 1] in swaps or t[i + 1] + t[i] in swaps:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = t[i]
    
    return True if s == t else False


if __name__ == "__main__":
    line = input()
    T = int(line)

    for i in range(T):
        line = input()
        k, n = tuple([int(e) for e in line.split()])

        swaps = []
        for j in range(n):
            swaps.append(input())
        s = input()
        t = input()
        print(judge(s,t,swaps))
