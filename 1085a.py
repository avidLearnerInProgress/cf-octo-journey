def right_left(mystr):
    lm = list(mystr)
    mid = len(lm) // 2
    if len(lm) % 2 == 0:
        mid = mid - 1
        print(lm[mid], end = '')
        i, j = mid - 1, mid + 1
        c = 0
        while c < mid:
            print(lm[j], end = '')
            print(lm[i], end = '')
            i -= 1
            j += 1
            c += 1
        print(lm[j], end = '')
    else:
        print(lm[mid], end = '')
        i, j = mid - 1, mid + 1
        c = 0
        while c < mid:
            print(lm[j], end = '')
            print(lm[i], end = '')
            i -= 1
            j += 1
            c += 1

right_left(str(input()))