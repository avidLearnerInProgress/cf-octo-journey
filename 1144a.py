from collections import Counter

def diverse_string(x):
    if x is None: return "No"
    if len(x) == 1: return "Yes"
    sx = sorted(x)
    flag1, flag2 = True, True
    for i in range(1, len(sx)):
        if abs(ord(sx[i-1]) - ord(sx[i])) > 1:
            flag1 = False
    
    sxc = Counter(sx)
    val_list = list(sxc.values())
    for ele in val_list:
        if ele > 1:
            flag2 = False
    
    if flag1 and flag2:
        return "Yes"
    else:
        return "No"


n = int(input())
for _ in range(n):
    print(diverse_string(str(input())))