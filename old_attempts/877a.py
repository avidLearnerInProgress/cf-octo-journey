def broken(mystr):
    
    match = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
    c1 = mystr.count(match[0])
    c2 = mystr.count(match[1])
    c3 = mystr.count(match[2])
    c4 = mystr.count(match[3])
    c5 = mystr.count(match[4])
    res = [c1, c2, c3, c4, c5]
    #print(res)
    if sum(res) == 1:
        return "YES"
    else:
        return "NO"
print(broken(str(input())))