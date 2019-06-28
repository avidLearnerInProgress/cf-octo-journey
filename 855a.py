y = int(input())
lz= []
j = 0
flag = True
for i in range(y):
    z = str(input())
    lz.append(z)
    for j in range(i+1):
        if lz[j] == lz[i]:
            flag = False
            break
    if j == i:
        print("NO")
    elif not flag:
        print("YES")
    else:
        print("NO")