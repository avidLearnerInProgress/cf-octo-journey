def translation(birlandish):
    b = birlandish
    if b is None or len(b) == 1:
        return b
    
    bl = list(b)
    bl = bl[::-1]
    return ''.join(bl)

berlandish = str(input())
birlandish = str(input())

res = translation(birlandish)
if res == berlandish: print("YES")
else: print("NO")