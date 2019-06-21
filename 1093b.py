def rearrange(mystr):
    if mystr is None:
        return None
    
    lm = list(mystr)
    if lm == lm[::-1]: #good string
        lms = sorted(lm)
        if lms == lm:
            return -1
        else: return ''.join(lms)
    else: #not good string 
        return mystr
        
n = int(input())
for _ in range(n):
    print(rearrange(str(input())))