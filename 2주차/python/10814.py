import sys
input = sys.stdin.readline

# 340ms
data = sorted([list(map(str, input().split())) for _ in range(int(input()))], key=lambda x: int(x[0]))
for item in data:
    print(*item)

# 276ms
for item in sorted([list(map(str, input().split())) for _ in range(int(input()))], key=lambda x: int(x[0])):
    print(*item)

# 104ms
print("".join(sorted([input() for _ in range(int(input()))], key=lambda x: int(x.split()[0]))))

# 100ms
sys.stdout.write("".join(sorted([input() for _ in range(int(input()))], key=lambda x: int(x.split()[0]))))
