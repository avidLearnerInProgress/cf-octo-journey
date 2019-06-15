n = int(input())
A, B, C = 0, 0, 0
while n > 0:
    a,b,c = map(int, input().split(' '))
    A += a
    B += b 
    C += c 
    n -= 1
if A == 0 and B == 0 and C == 0:
    print("YES")
else:
    print("NO")
