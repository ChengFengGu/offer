# 题目：输入一个字符串，要求将它分割成若干子字符串，使每个子字符串都是回文。请列出所有可能的分割方法。例如，输入"google"，将输出3种符合条件的分割方法，分别是["g"，"o"，"o"，"g"，"l"，"e"]、["g"，"oo"，"g"，"l"，"e"]和["goog"，"l"，"e"]。

def judge(string:str):
    mid = len(string) // 2
    flag = True
    for i in range(mid):
        if string[i] != string[-(i+1)]:
            flag = False
    return flag


def helper(string:str,index:int,container:str,result:list):
    
    if index <= len(string):
        pass

    pass


def generate(string:str):
    pass