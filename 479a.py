def max_calc(a, b, c):
    ans = a + b + c
    ans = max(ans, ((a + b) * c))
    ans = max(ans, (a * (b + c)))
    ans = max(ans, (a * b * c))
    print(ans)

max_calc(int(input()), int(input()), int(input()))