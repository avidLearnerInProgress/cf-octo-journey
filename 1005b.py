def delete_from_left(a, b):
    if a is None and b is None: return 0
    if a is None: return len(b)
    if b is None: return len(a)
    
    if a[-1] != b[-1]:
        return len(a) + len(b)
    
    i, j, w = len(a)-1, len(b)-1, 0
    while i>=0 and j>=0:
        if a[i] == b[j]:
            w += 1
        elif a[i] != b[j]:
            break
        else:
            pass
        i -= 1
        j -= 1
    return len(a) + len(b) - 2*w

a, b = str(input()), str(input())
print(delete_from_left(a, b))
                