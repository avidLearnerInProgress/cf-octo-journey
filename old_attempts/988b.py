def substring_sort(slist):
    if slist is None:
        return "NO"
    lengths = [len(x) for x in slist]
    sortedxs = sorted(slist, key = len)
    mxlenstr = sortedxs[-1]
    ok = True
    for x in range(0, len(sortedxs)-1):
        if str(sortedxs[x+1]).find(str(sortedxs[x])) == -1:
            ok = False
    if not ok:
        return ("NO", None)
    else:
        return ("YES", sortedxs)

n = int(input())
ls = []
for i in range(n):
    ls.append(str(input()))
res, sorte = substring_sort(ls)
print(res)
if sorte is not None:
    for x in sorte:
        print(x)