def k_palindrome(mystr, k):
    if mystr is None or k == 0:
         return "NO"
    n = len(mystr)
    if n % k != 0: print("NO")
    else:
        for i in range(0, n, n//k):
            a = mystr[i:i+n//k]
            if a != a[::-1]:
                print("NO")
                break
        else:
            print("YES")

x = str(input())
y = int(input())
k_palindrome(x, y)