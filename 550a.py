def nonoverlapping(mystr):
    if mystr is None: return "NO"
    x1, x2 = 0, 0
    
    x1 = mystr.find("AB")
    x2 = mystr.find("BA", x1 + 2)
    y1 = mystr.find("BA")
    y2 = mystr.find("AB", y1 + 2)
    
    if (x1!=-1 and x2!=-1) or (y1!=-1 and y2!=-1):
        return "YES"
    else:
        return "NO"
    

my = str(input().strip())
print(nonoverlapping(my))
