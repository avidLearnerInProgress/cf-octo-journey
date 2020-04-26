from collections import Counter
def equality(s, n, k):
    if s is None: return 0
    unq= set(s)
    if len(unq) != k:
        return 0
    vl = list(Counter(s).values())
    minCount = min(vl)
    
    for i in range(k):
        minCount = min(vl[i], minCount)
    
    minCount *= k
    return minCount

n, k = map(int, input().split())
equal = list(str(input()))
print(equality(equal, n, k))