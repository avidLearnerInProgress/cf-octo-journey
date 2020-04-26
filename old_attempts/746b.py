def decoding(mystr):
    if mystr is None: return None
    if len(mystr) <= 2: return mystr
    res = ''
    for i in range(len(mystr)):
        if (len(mystr) - i) % 2 == 0:
            res = res + mystr[i]
        else:
            res = mystr[i] + res
    return res[::-1]
     
n = int(input())
my = str(input())
print(decoding(my)) 