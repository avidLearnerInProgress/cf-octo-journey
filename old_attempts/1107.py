def sequence_dividing(sequence):
    if sequence is None: return ("NO", None)
    if len(sequence) == 2 and sequence[0] >= sequence[1]:
        print("NO")
    else:
        print("YES")
        print(2)
        print(str(sequence[0]) + ' ' + str(sequence[1:]))

n = int(input())
for _ in range(n):
    _ = int(input())
    sequence_dividing(str(input()))