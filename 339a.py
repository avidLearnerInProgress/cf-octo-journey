def helpful_maths(myStr):
    if len(myStr) <= 1:
        print(myStr)
        return
    summans = list(myStr.split('+'))
    #print(summans)
    summans_s = sorted(summans)
    res = summans_s[0] + '+'
    print(str(res) + '+'.join(summans_s[1:]))
    
value = str(input())
helpful_maths(value)