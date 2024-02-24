def pow(x, n):
    if x == 0:
        return 0
    preValues = {}
    val, preValues = calculatePow(x, abs(n), preValues)
    if n > 0:
        return val
    else:
        return 1 / val


def calculatePow(x, n, preValues):
    
    if n == 0:
        preValues[0] = 1
        return 1, preValues
    elif n == 1:
        preValues[1] = x
        return x, preValues
    if n in preValues:
        return preValues[n], preValues
    else:
        mid = n // 2
        lValue, _ = calculatePow(x, mid, preValues)
        rValue, _ = calculatePow(x, n - mid, preValues)
        val = lValue * rValue
        preValues[n] = val
        return val, preValues

    
print(pow(2, -4))
