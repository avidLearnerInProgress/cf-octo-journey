def different_is_good(mystr):
    if len(mystr) > 26: 
        print(-1)
        return
    
    hash_, diff = [0] * 128, 0
    for char in mystr:
        if hash_[ord(char)] == 1:
            diff += 1 
        else:
            hash_[ord(char)] = 1
    print(diff)


_ = int(input())
different_is_good(str(input()))