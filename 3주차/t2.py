# 10816 숫자 카드 2
# https://www.acmicpc.net/problem/10816
import sys
from collections import Counter
input = sys.stdin.readline

n, data, m = int(input()), Counter(list(map(int, input().split()))), input()
print(*[data[num] for num in list(map(int, input().split()))])