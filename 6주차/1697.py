# 숨바꼭질
# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k:
        print(visited[x])
        break
    for i in (x+1, x-1, x*2):
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = visited[x] + 1
            queue.append(i)