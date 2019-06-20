def photobooks(a):
    if a is None or len(a) == 0:
        return 0
    return (len(a) + 1) * 25 + 1

print(photobooks(str(input())))