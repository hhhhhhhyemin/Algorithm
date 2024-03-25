import sys
d={}
cnt = 0
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    data = sys.stdin.readline().rstrip()
    d[data] = True

for _ in range(m):
    data = sys.stdin.readline().rstrip()
    if data in d:
        cnt += 1
print(cnt)