# 10026 적록색약
# https://www.acmicpc.net/problem/10026
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
grid1 = []
grid2 = []
for _ in range(n):
    temp = input().strip()
    grid1.append(list(temp))
    grid2.append(list(temp.replace("R", "G")))

directions = [(1,0), (-1,0), (0,1), (0,-1)]
def dfs(x, y, color, grid):
    visited[x][y] = 1
    for i in range(4):
        dx = x + directions[i][0]
        dy = y + directions[i][1]
        if 0<=dx<n and 0<=dy<n and not visited[dx][dy]:
            if grid[dx][dy] == color:
                dfs(dx, dy, color, grid)

cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, grid1[i][j], grid1)
            cnt += 1
print(cnt, end = " ")

cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, grid2[i][j], grid2)
            cnt += 1
print(cnt)