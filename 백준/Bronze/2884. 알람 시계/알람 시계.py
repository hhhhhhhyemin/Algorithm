Hour, Min = map(int, input().split())
if Min < 45 :
    if Hour == 0 :
        Hour = 23
        Min += 60
    else : 
        Hour -= 1
        Min += 60
print(Hour, Min-45)