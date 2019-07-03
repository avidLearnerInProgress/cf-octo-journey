import sys
INT_MAX = sys.maxsize  
def calcDist(mystr, y):
    dist = 0
    for i in range(len(mystr)):
        c = abs(ord(mystr[i]) - ord(y[i]))
        dist += min(c, 26-c)
    return dist
    
 
def substr_manip(s, y):
    if s is None:
        return 0
    su = list(s)
    res = INT_MAX
    for i in range(len(su)-3):
        curr = su[i:i+4]
        cd = calcDist(curr, y)
        res = min(cd, res)
    print(res)
 
_ = int(input())
substr_manip(str(input()), "ACTG")