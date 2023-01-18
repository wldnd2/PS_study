# 2910 빈도정렬
# https://www.acmicpc.net/problem/2910
import sys
from collections import Counter
input = sys.stdin.readline

input()
print(*[item[0] for item in Counter(map(int, input().split())).most_common() for ind in range(item[1])])