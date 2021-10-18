def helper(n,index,container,result):
    if index == 2*n:
        left_num = 0
        right_num = 0
        for e in container:
            if e == "(": left_num += 1
            if e == ")": right_num += 1
        if left_num == right_num:
            result.append(container)
    else:
        


def generate(n:int):
    pass