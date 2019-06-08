def findCase(myStr):
    if len(myStr) <= 1:
        return myStr
    list_case = list(myStr)
    upper_ct, lower_ct = 0,0
    for char in list_case:
        if char.isupper():
            upper_ct += 1
            continue
        if char.islower():
            lower_ct += 1
            continue
    if(lower_ct >= upper_ct):
        return str.lower(myStr)
    else:
        return str.upper(myStr)
ip = input()
print(findCase(ip))