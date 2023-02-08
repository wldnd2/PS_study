# 2178 미로 탐색
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

queue = deque([(0,0)])
next_directions = [(0,1), (1,0), (-1, 0), (0, -1)]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = next_directions[i]
        if 0<=x+nx<n and 0<=y+ny<m and graph[x+nx][y+ny] == 1:
            graph[x+nx][y+ny] = graph[x][y] + 1
            queue.append((x+nx, y+ny))

print(graph[-1][-1])