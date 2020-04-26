'''
if the number of distinct characters in one's user name is odd, 
then he is a male, otherwise she is a female.
If it is a female by our hero's method, print "CHAT WITH HER!" 
(without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).
'''

def recognize(myStr):
    if len(myStr) <= 1:
        print("IGNORE HIM!")
        return
    distinct_char = [0] * (256)
    count_dist = 0
    for c in range(len(myStr)):
        h = ord(myStr[c])
        if distinct_char[h] == 1:
            pass
        else:
            distinct_char[h] = 1
            count_dist += 1
    
    if count_dist % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
    return
    
value = str(input())
recognize(value)