# 4358 생태학
# https://www.acmicpc.net/problem/4358
import sys
from collections import Counter

data = Counter(sys.stdin.read().split('\n')[:-1])
total = sum(data.values())
for item in sorted(data.items()):
    print("{} {:.4f}".format(item[0], item[1]/total * 100))