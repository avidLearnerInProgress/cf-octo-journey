def file_name(x):
    if x is None: print(0)
    x_count, count_xxx = x.count("x"), 0
    if(x_count == 0):
        return 0
    for i in range(2, len(x)):
        if x[i-2:i+1] == "xxx":
            count_xxx += 1
    return count_xxx

s = int(input())
x_str = str(input())
print(file_name(x_str))