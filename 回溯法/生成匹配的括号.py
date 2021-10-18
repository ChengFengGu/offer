def helper(n, index, container, result):
    if index == 2 * n:
        left_num = 0
        right_num = 0
        for e in container:
            if e == "(":
                left_num += 1
            if e == ")":
                right_num += 1
        if left_num == right_num:
            result.append(container.copy())
    else:
        container.append("(")
        helper(n, index + 1, container, result)
        container.pop()

        container.append(")")
        helper(n, index + 1, container, result)
        container.pop()


def generate(n: int):
    container = []
    result = []
    helper = helper(n, index)
