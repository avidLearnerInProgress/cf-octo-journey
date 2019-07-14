def trim(mystr):
    if mystr is None:
        return
    flag = False    
    my = list(mystr)
    for i in range(len(my)-1):
        if my[i] > my[i+1]:
            my[i] = '$' #set marker and flag to true meaning you found larger before smaller that is char to minimize
            flag = True
            break
    
    if not flag:
        res = my[:-1]
        print(''.join(res))
    else:
        for c in my:
            if c != '$':
                print(c, end = '')
 
a = int(input())
trim(str(input()))                
