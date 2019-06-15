def telephone_number(mystr):
    if mystr is None: return "NO"
    x= mystr.find('8')
    if x != -1 and abs(len(mystr) - x) >= 11:
        return "YES"
    return "NO"

n = int(input())
for i in range(n):
    _ = int(input())
    print(telephone_number(str(input())))