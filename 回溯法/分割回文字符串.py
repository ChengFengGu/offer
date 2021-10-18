# 题目：输入一个字符串，要求将它分割成若干子字符串，使每个子字符串都是回文。请列出所有可能的分割方法。例如，输入"google"，将输出3种符合条件的分割方法，分别是["g"，"o"，"o"，"g"，"l"，"e"]、["g"，"oo"，"g"，"l"，"e"]和["goog"，"l"，"e"]。


def judge(string: str):
    if len(string) == 0:
        return False
    if len(string) == 1:
        return True
    mid = len(string) // 2
    flag = True
    for i in range(mid):
        if string[i] != string[-(i + 1)]:
            flag = False
    return flag


def helper(string: str, index: int, container: str, result: list):

    if judge(container):
        result.append(container)
    if index < len(string):  # 从当前字符串算起，一共有多少个
        for j in range(index,len(string)):
            container = ""
            container += string[index]
            helper(string, index + 1, container, result)
            container = container[:-1]


def generate(string: str):
    container = ""
    result = []
    helper(string, 0, container, result)
    return result


if __name__ == "__main__":
    print(generate("google"))
