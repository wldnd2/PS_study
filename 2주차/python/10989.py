import sys
input = sys.stdin.readline

num_list = [0] * 10001
for _ in range(int(input())):
    num_list[int(input())] += 1

for i in range(10001):
    if num_list[i]:
        for j in range(num_list[i]):
            print(i)