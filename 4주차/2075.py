# 2075 n번째 큰수
# https://www.acmicpc.net/problem/2075
# 알고리즘 : 슬라이딩 윈도우
# https://learning-e.tistory.com/36
import sys
input = sys.stdin.readline

data = []
for i in range(n := int(input())):
    data.extend(list(map(int, input().split())))
    # data += list(map(int, input().split()))
    data = sorted(data, key= lambda x: -x)[:n]
print(data[-1])