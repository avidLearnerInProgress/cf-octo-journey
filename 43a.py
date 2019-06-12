from collections import Counter
goals = []
T = int(input())
if T == 1:
    print(str(input().strip()))
else:
    for i in range(T):
        goals.append(str(input().strip()))
    
    keys = Counter(goals).keys()
    values = Counter(goals).values()
    if(len(keys))<=1:
        k1, = keys
        print(k1)
    else:
        k1, k2 = keys
        x1, x2 = values
        print(k1) if x1>x2 else print(k2)
        