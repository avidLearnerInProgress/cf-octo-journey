from string import ascii_lowercase
ip = int(input())
pangram_str = str(input())
if(set(ascii_lowercase) - set(pangram_str.lower()) == set([])) == True:
    print("YES")
else:
    print("NO")
     