def isPerfectSquare(a):
  left = 0
  right = a
  while(left + 1 < right):
    mid = (left + right) // 2
    if mid * mid == a:
      return True, a
    elif mid * mid < a:
      left = mid
    else:
      right = mid
  print(left, right)
  if right * right == a:
    return True, a
  
  return False, a


def main():
 
  print("isPerfectSquare is ---> " + str(isPerfectSquare(25)))
  print("isPerfectSquare is ---> " + str(isPerfectSquare(16)))
  print("isPerfectSquare is ---> " + str(isPerfectSquare(10)))
  print("isPerfectSquare is ---> " + str(isPerfectSquare(9)))
  print("isPerfectSquare is ---> " + str(isPerfectSquare(3)))
  print("isPerfectSquare is ---> " + str(isPerfectSquare(1)))
  print("isPerfectSquare is ---> " + str(isPerfectSquare(100)))


if __name__ == "__main__":
    main()
