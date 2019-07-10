def petals(mystr):
    if mystr is None:
        return "No"
    
    xd = set(["BAC", "ABC", "ACB", "BCA", "CAB", "CBA"])
    for i in range(len(mystr) - 2):
        cu = mystr[i] + mystr[i+1] + mystr[i+2] 
        if cu in xd:
            return "Yes"
    
    return "No"

print(petals(str(input())))