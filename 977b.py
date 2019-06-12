def two_gram(x, n):
    if x is None: return None
    
    l, count_m = len(x), {}
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            cur = x[i] + x[j]
            curr = x.count(cur)
            count_m[cur] = curr
    
    #for k,v in count_m.items():
    #    print(k, v)
    
    count_m = sorted(count_m.items(), key = lambda kv:(kv[1], kv[0]))
    print(count_m[-1][0])

n = int(input())
x = str(input())
two_gram(x, n)