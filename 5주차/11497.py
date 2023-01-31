# 11497 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497
import sys
from collections import deque
input = sys.stdin.readline

data = []
for _ in range(n := int(input())):
    input()
    temp = sorted(list(map(int, input().split())), key=lambda x:-x)
    deq = deque()
    for idx, item in enumerate(temp):
        if idx%2 == 0: deq.appendleft(item)
        else: deq.append(item)
    data.append(list(deq))

for idx in range(n):
    temp = [abs(data[idx][i]-data[idx][i+1]) for i in range(len(data[idx])-1)]
    print(max(temp))

# 정석 풀이
# for i in range(T := int(input)):
#     N=int(input())
#     trees=list(map(int,input().split()))
#     trees.sort()
#     result=0
#     for j in range(2, N):
#         result=max(result,abs(trees[j]-trees[j-2]))
#     print(result)