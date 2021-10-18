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
        if container not in result:
            result.append(container)
    if index < len(string):  # 一共有多少个字串，都要得到
        container = ""
        for j in range(index, len(string) + 1):
            helper(string, index + 1, container + string[index:j], result)


def generate(string: str):
    container = ""
    result = []
    helper(string, 0, container, result)
    return sorted(result)


if __name__ == "__main__":
    print(generate("google"))


# 自己有改动： https://weread.qq.com/web/reader/4e132bc07263ff664e11075kb5332110237b53b3a3d68d2

