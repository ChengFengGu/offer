def helper(matrix: list, index: int, n: int, result: list, path: list, cost: int,costs=[]):

    if matrix[index][n - 1] != -1:
        path_bak = path
        path_bak.append(n - 1)
        result.append(path_bak)

        cost_bak = cost
        cost_bak +=  matrix[index][n - 1]
        costs.append(cost_bak)
    elif index < n:
        reached_nodes = []
        for j in range(n):
            if matrix[index][j] != -1:
                helper(matrix, index + 1, n, result, path, cost)
                path.append(j)
                cost = cost + matrix[index][j]
                helper(matrix, index + 1, n, result, path, cost)
                path.pop()
                cost = cost - matrix[index][j]


if __name__ == "__main__":
    line = input()

    n, m = tuple(int(e) for e in line.split())

    matrix = [[-1 for _ in range(n)] for i in range(n)]
    matrix_time = [[-1 for _ in range(n)] for i in range(n)]
    for i in range(1, m + 1):
        line = input()
        src, dst, cost, time = tuple(int(e) for e in line.split())
        matrix[src - 1][dst - 1] = cost
        matrix[dst - 1][src - 1] = cost

        matrix_time[src - 1][dst - 1] = time
        matrix_time[dst - 1][src - 1] = time

    paths = []
    cost = 0
    costs = []
    helper(matrix, 0, n, paths, [], cost,costs)

    min_cost = min(costs)
    index = costs.index(min_cost)
    
    path = paths[index]
    
    total_time = 0
    for i in range(len(path)):
        total_time += matrix_time[i][path[i]]

    print(f"{min_cost} {total_time}")

    # for i in range(n):
    #     reached_nodes = []
    #     costs = []
    #     for j in range(n):
    #         if matrix[i][j] != -1 and j not in path:
    #             reached_nodes.append(j)
    #             costs.append(matrix[i][j])
    #     cost = min(costs)
    #     index = costs.index(cost)
    #     node = reached_nodes[index]

    #     dp[i] = sum(dp[0:i]) + cost
    #     path.append(node)

    # print("temp done")
