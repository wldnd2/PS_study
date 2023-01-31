# 13305 주유속
# https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

n = int(input())-1
oil = list(map(int, input().split()))
city = list(map(int, input().split()))[:-1]

start = oil[0]*city[0]
stop = city[0]
for i in range(1, n):
    if stop > city[i]:
        stop = city[i]
    start += stop*oil[i]
print(start)