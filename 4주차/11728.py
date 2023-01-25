# 11728 배열 합치기
# https://www.acmicpc.net/problem/11728
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(*sorted(sum([list(map(int, input().split())) for _ in range(2)], [])))