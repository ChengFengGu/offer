
if __name__ == '__main__':
    line = input()
    T = int(line)
    for i in range(T):
        line = input()
        k,n = tuple([int(e) for e in line.split()])
        for j in range(n):
            