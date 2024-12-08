def findNthRootOf(x, nth):
    
    left = 0
    right = (x//nth)+1
    while(left + 1 < right):
        print("FNR ", left, right)
        mid = (left + right) // 2
        newX = calPow(mid, nth)
        if newX == x:
            return mid
        elif x > newX:
            left = mid
        else:
            right = mid
        print("newX", newX)
    print("last", left, right, newX)
    if newX-calPow(left, nth)<newX-calPow(right, nth):
        return left
    else:
        return right

    
def calPow(num, pOf):
    if pOf == 0:
        return 1
    if num == 0:
        return 0
    res = calPow(num * num, pOf // 2)
    return num * res if pOf % 2 else  res


if __name__ == "__main__":
    ans = 4
    nth = 6
    val = calPow(ans, nth)
    new_ans = findNthRootOf(val , nth)
    print(ans, new_ans, val, nth)
