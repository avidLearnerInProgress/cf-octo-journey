def caps_lock(mystr):
    if len(mystr) > 1:
        if str.upper(mystr) == mystr:
            return str.lower(mystr)
        elif str.upper(mystr[1:]) == mystr[1:]:
            return str(str.upper(mystr[0]) + str.lower(mystr[1:]))
        else:
            return mystr
    else:
        return str.swapcase(mystr)
mixed_str = str(input())
print(caps_lock(mixed_str))