import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

cnt = {}
for card in cards:
    if card in cnt:
        cnt[card] += 1
    else: 
        cnt[card] = 1
for target in candidate:
    result = cnt.get(target)
    if result == None:
        print(0, end=' ')
    else:
        print(result, end=' ')