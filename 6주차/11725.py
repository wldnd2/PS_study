# 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(graph, start):
    global check
    for node in graph[start]:
        if check[node] == 0:
            check[node] = start
            dfs(graph, node)

n = int(input())
graph = [[] for _ in range(n+1)]
check = [0]*(n+1)
for _ in range(n-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
dfs(graph, 1)
for item in check[2:]:
    print(item)

# def dfs(graph, start):
#     discoverd = []
#     stack = [start]
#     while stack:
#         v = stack.pop()
#         if v not in discoverd:
#             for w in graph[v]:
#                 stack.append(w)
#     return discoverd
