def check_palindrome(x):
    if x is None: print(0)
    l_x = x
    i, j = 0, len(l_x) - 1
    count_ueq = 0
    
    for i in range(0, len(l_x)//2):
        if l_x[i] != l_x[j]:
            if count_ueq > 1:
                return "NO"
            count_ueq += 1
        j -= 1
    
    if len(l_x) % 2 == 0 and count_ueq == 1:
        return "YES"
    elif len(l_x) % 2 == 1 and count_ueq <= 1:
        return "YES"
    else:
        return "NO"
    
x_str = str(input())
print(check_palindrome(x_str))