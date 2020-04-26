def k_bananas(k, n, w):
    su,i = 0,1
    while(w>0):
        su += (i*k)
        i+=1
        w-=1
    if n > su:
        print(0)
    else:
        print(abs(su-n))

k,n,w = map(int, input().split(' '))
k_bananas(k, n, w)