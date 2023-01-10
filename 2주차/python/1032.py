n = int(input())
for i in zip(*[input().strip() for _ in range(n)]):
    if i == (i[0],)*n: print(i[0], end=' ')
    else: print("?", end=' ')