def capitalisation(myStr):
    if len(myStr) <= 1:
        print(myStr.upper())
        return
    capitalise = list(myStr)
    to_capital = str(capitalise[0].upper())
    print(to_capital + ''.join(capitalise[1:]))
    
value = str(input())
capitalisation(value)