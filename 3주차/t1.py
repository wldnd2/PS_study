# 5588 별자리 찾기
# https://www.acmicpc.net/problem/5588
import sys
from collections import Counter
input = sys.stdin.readline

m = int(input())
data = [list(map(int, input().split())) for i in range(m)]
n = int(input())
star = [list(map(int, input().split())) for i in range(n)]
print(*Counter([(star[j][0] - data[i][0], star[j][1] - data[i][1]) for i in range(m) for j in range(n)]).most_common()[0][0])
