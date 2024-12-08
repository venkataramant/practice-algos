def pow(x, n):
    if x == 0:
        return 0
    else:
        preValues = {}
        newN = abs(n)
        midN = abs(n) // 2
        for index in range(0, midN+2):
            if index==0:
                preValues[0] = 1
            elif index==1:
                preValues[1] = x
            else:
                mid = index // 2
                lValue = preValues[mid]
                rValue = preValues[index - mid]
                preValues[index] = lValue * rValue
        preValues[newN] = preValues[midN] * preValues[newN - midN]
        if n > 0:
            return preValues[newN]
        else:
            return 1 / preValues[newN]


def pow2(x, n):
    if x == 0:
        return 0
    preValues = {}
    preValues[0] = 1
    preValues[1] = x
    
    for index in range(1, abs(n) + 1):
        mid = index // 2
        lValue = preValues[mid]
        rValue = preValues[index - mid]
        preValues[index] = lValue * rValue
    if n > 0:
        return preValues[abs(n)]
    else:
        return 1 / preValues[abs(n)]


print(pow(0.00001,2147483647))
