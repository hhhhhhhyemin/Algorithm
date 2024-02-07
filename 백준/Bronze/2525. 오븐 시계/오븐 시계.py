hour, min = map(int, input().split())
timer = int(input())
hour += timer // 60
min += timer % 60
if min >= 60 :
    hour += 1
    min -= 60
if hour >= 24 :
    hour -= 24
print(hour, min)