m, n = map(str, input().split())
m, n = m.lower(), n.lower()

def serial_killer(x, y):
    global m, n
    if x == m:
        m = y
        print(str(m) + ' ' + str(n))
    if x == n:
        n = y
        print(str(m) + ' ' + str(n))
    
    
p = int(input())
print(str(m) + ' ' + str(n))
for _ in range(p):
    x, y = map(str, input().split())
    x, y = x.lower(), y.lower()
    serial_killer(x, y)