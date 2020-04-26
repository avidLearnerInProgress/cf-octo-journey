def find_first(mystr):
    p1 = int(mystr.index('G'))
    p2 = int(mystr.index('T'))
    #print(p1, p2)
    diff = abs(p1 - p2)
    if p1 < p2:
        return (p1, diff)
    else:
        return (p2, diff)
    
def grasshopper_ostap(mystr, k):
    if mystr is None or k is None or k is 0:
        return "NO"
    f1, f2 = False, False
    pos, diff = find_first(mystr)
    #print(pos, diff)
    if diff % k != 0:
        return "NO"
    cnt = 0
    for i in range(pos, len(mystr), k):
        #print(mystr[i])
        if mystr[i] == '#':
            return "NO"
        elif mystr[i] == 'G':
            #print(i)
            cnt += 1
            f1 = True
            if cnt == 2:
                break
        elif mystr[i] == 'T':
            #print(i)
            cnt += 1
            f2 = True
            if cnt == 2:
                break
    if f1 and f2:
        return "YES"
    else:
        return "NO"

_, k = map(int, input().split())
print(grasshopper_ostap(str(input()), k))