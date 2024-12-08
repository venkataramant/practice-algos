# from youtube
def pow(x, n):
    
    val = calculatePow(x, abs(n))
    if n > 0:
        return val
    else:
        return 1 / val


def calculatePow(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    res = calculatePow(x * x, n // 2) # res=calculatePow(x,n//2) , res=res*res or pass res*res to function
    return x * res if n % 2 else res

    
print(pow(2, 5))
