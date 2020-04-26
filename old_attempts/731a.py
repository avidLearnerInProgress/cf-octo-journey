LENGTH = 26
def min_distance(a, b):
    return min(abs(ord(a) - ord(b)), LENGTH - abs(ord(a) - ord(b)))

def night_at_museum(mstr):
    if mstr == None:
        return None
    lstr = list(mstr)
    rotation = min_distance(lstr[0], 'a')
    #print(rotation)
    for c in range(1, len(lstr)):
        #print(lstr[c-1], lstr[c])
        rotation += min_distance(lstr[c-1], lstr[c])
    
    return rotation

mystr = str(input().strip())
print(night_at_museum(mystr))