# 自己的思路 ： 有明显不完善的地方

# def helper(n, index, container, result):
#     if index == 2 * n:
#         left_num = 0
#         right_num = 0
#         for e in container:
#             if e == "(":
#                 left_num += 1
#             if e == ")":
#                 right_num += 1
#         if left_num == right_num:
#             result.append(container.copy())
#     else:
#         container.append("(")
#         helper(n, index + 1, container, result)
#         container.pop()

#         container.append(")")
#         helper(n, index + 1, container, result)
#         container.pop()


# 剑指offer https://weread.qq.com/web/reader/4e132bc07263ff664e11075kb5332110237b53b3a3d68d2
def helper(left: int, right: int, parethesis, result):
    if left == 0 and right == 0:
        result.append(parethesis)
        return
    if left > 0:
        helper(left - 1, right, parethesis + "(", result)
    if left < right:
        helper(left, right - 1, parethesis + ")", result)


def generate(n: int):
    container = ""
    result = []
    helper(n, n, container, result)
    return result


if __name__ == "__main__":
    print(generate(3))
