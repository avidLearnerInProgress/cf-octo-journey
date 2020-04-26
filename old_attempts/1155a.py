def is_lexicographically_less(s, y):
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            print("YES")
            print(str(i) + " " + str(i+1))
            return
    print("NO")
a = int(input())
x = str(input())
is_lexicographically_less(x, a)