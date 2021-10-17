'''
Author: your name
Date: 2021-10-17 23:20:47
LastEditTime: 2021-10-17 23:28:54
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
        matrix[src][dst] = 1
        matrix[dst][src] = 1
        
    
    containers = []
    def dfs(node,matrix,container:list):
        container.append(node)
        for i in 
    
    