'''
Author: your name
Date: 2021-10-17 23:20:47
LastEditTime: 2021-10-17 23:41:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /offer/生日聚会.py
'''


if __name__ == "__main__":
    N = int(input())
    data = eval(input())
    
    num = 1
    
    matrix = [[0 for _ in range(N)] for i in range(N)]
    
    for src,dst in data:
        matrix[src-1][dst-1] = 1
        matrix[dst-1][src-1] = 1
        
    
    containers = set()
    
    
    def dfs(node,matrix,container:set):
        origin_len = len(container)
        container.add(node)
        after_len = len(container)
        if origin_len == after_len:
            return container
        for i in range(N):
            if matrix[node][i] == 1:
                container = dfs(i,matrix,container)
        return container
    
    flag = True
    idx = 0
    while flag:
        if sum([len(e) for e in containers]) == N:
            flag = False
        else:
            containers.add(dfs(idx,matrix,set()))
            
    print(len(containers))
            
    

    
    