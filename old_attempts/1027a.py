def is_palindromic(mystr):
    l = len(mystr)
    for i in range(l):
        dist = abs(ord(mystr[i]) - ord(mystr[l - i - 1]))
        if dist > 2 or dist % 2 == 1:
            return False
    return True
    
x = int(input())
for i in range(x):
    tp = int(input())
    if is_palindromic(str(input())):
        print("YES")
    else:
        print("NO")