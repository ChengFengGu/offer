# ==========================================
# 题目：输入一个只包含'0'和'1'的字符串，其中，'0'可以翻转成'1'，'1'可以翻转成'0'。请问至少需要翻转几个字符，才可以使翻转之后的字符串中所有的'0'位于'1'的前面？翻转之后的字符串可能只包含字符'0'或'1'。例如，输入字符串"00110"，至少需要翻转一个字符才能使所有的'0'位于'1'的前面。可以将最后一个字符'0'翻转成'1'，得到字符串"00111"
# ==========================================

# 状态转移方程

# S(i-1) = 0 输入:S(i) = 0 的时候, f(i) = f(i-1) g(i) = min(f(i-1),g(i-1)) + 1
# S(i-1) = 0 输入:S(i) = 1 的时候, f(i) = f(i-1) + 1   g(i) = min(f(i-1),g(i-1))

# S(i-1) = 1 输入:S(i) = 0 的时候, f(i) = f(i-1) + 1   g(i) = min(f(i-1),g(i-1)) + 1
# S(i-1) = 1 输入:S(i) = 1 的时候, f(i) = f(i-1) + 1   g(i) = min(f(i-1),g(i-1))

# 以00110 为例:

# i = 0 时 输入为0: f(0) = 0 g(0) = 1
# i = 1 时 输入为0 S(i-1) 为 0 : f(1) = f(0) = 0 , g(1) = min(0,1) + 1 = 1
# i = 2 时 输入为1 S(i-1) 为 0 : f(2) = f(1) + 1 = 1 , g(2) = min(0,1) = 0
# i = 3 时 输入为1 S(i-1) 为 1 : f(3) = f(2) + 1 = 2 , g(3) = min(0,1) = 0
# i = 4 时 输入为0 S(i-1) 为 1 : f(4) = f(3) + 1 = 3 , g()


if __name__ == "__main__":
    pass