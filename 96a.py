def dangerous_positions(myStr):
    if len(myStr) <= 1:
        return False
    count_dangerous = 1
    for c in range(1, len(myStr)):
        if myStr[c] == myStr[c-1]:
            count_dangerous += 1
            #print(count_dangerous, end = '# ')
            if count_dangerous == 7:
                return True
        else:
            count_dangerous = 1
    return False
    
value = str(input())
if dangerous_positions(value): print("YES")
else: print("NO")