def merge(a: list, b: list):
    # if a == None and b == None:
    #     return []
    # elif a == None:
    #     return b
    # elif b == None:
    #     return a
    merged = []
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # 剩余的放进来
    merged.extend(a[i:])
    merged.extend(b[j:])


def sort(c: list):
    if len(c) <= 1:
        return c
    mid = len(c) // 2
    if mid == 0 or mid == len(c)-1:
        return c
    
    a = sort(c[:mid])
    b = sort(c[mid:])
    return merge(a,b)

if __name__ == "__main__":
    result = sort([1,3,2,5,4])
    print(result)