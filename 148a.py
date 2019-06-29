def insomnia(k, l, m, n, d):
    if d<k and d<l and d<m and d<n:
        print(0)
        return
    if k==1 or l==1 or m==1 or n==1:
        print(d)
        return
    harm = 0
    for i in range(1, d+1):
        if i%k == 0 or i%m==0 or i%l==0 or i%n==0:
            harm += 1
    print(harm)
    return

k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())    
insomnia(k,l,m,n,d)