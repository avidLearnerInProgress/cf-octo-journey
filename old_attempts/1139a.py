def even(mystr):
    if mystr is None:
        return None 
    eve_cnt = 0
    for i in range(len(mystr)):
        if int(mystr[i]) % 2 == 0:
            eve_cnt += (i + 1)
    return eve_cnt

n = int(input())
mystr = str(input())
print(even(mystr))