def keyboard_layouts(a,b,c):
    if a is None or b is None or c is None:
        return None
    search = c.lower()
    for i in range(len(search)):
        if search[i].isdigit():
            print(search[i], end = '')
        else:
            x = a.find(search[i])
            if c[i].isupper():
                print(b[x].upper(), end = '')
            else:
                print(b[x], end = '')

keyboard_layouts(str(input()), str(input()), str(input()))