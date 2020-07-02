T = int(input())
for t in range(1, T + 1):
    str1 = input()
    res = []
    isOpen = 0
    for i in range(0, len(str1)):
        x = int(str1[i])
        if isOpen < x:
            res.append('(' * (x - isOpen))
        if x < isOpen:
            res.append(')' * (isOpen - x))
        isOpen = x
        res.append(str1[i])
    res.append(')' * isOpen)
    print("Case #{}: {}".format(t, ''.join(res)))
    