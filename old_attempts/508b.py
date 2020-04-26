def currency(s):
    if s is None: return None
    ls = list(s)
    n = ind = len(ls) - 1
    for i in range(len(ls)):
        if int(ls[i])%2 == 0:
            ind = i
            if int(ls[-1]) > int(ls[i]):
                break
    if n == ind:
        return -1
    else:
        ls[ind], ls[-1] = ls[-1], ls[ind]
        return (''.join(ls))

mystr = str(input())
print(currency(mystr))  