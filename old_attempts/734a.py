def game(mystr):
    a = mystr.count("A")
    b = mystr.count("D")
    
    if a > b:
        return "Anton"
    elif a == b:
        return "Friendship"
    else:
        return "Danik"

x = int(input())
ip = str(input())
print(game(ip))