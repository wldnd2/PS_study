import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data1 = [list(map(int, input().split())) for _ in range(n)]
data2 = [list(map(int, input().split())) for _ in range(n)]
for one, two in zip(data1, data2):
    for i, j in zip(one, two):
        print(i+j, end = " ")
    print()
