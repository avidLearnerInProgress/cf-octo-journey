def vowel_consonant(x1, x2):
    if x1 is None or x2 is None: return "No"
    if len(x1) != len(x2): return "No"
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(x1)):
        if x1[i] in vowels and x2[i] in vowels:
            continue
        
        elif x1[i] not in vowels and x2[i] not in vowels:
            continue
        
        else:
            return "No"
    
    return "Yes"

x1, x2 = str(input()), str(input())
print(vowel_consonant(x1, x2))
    