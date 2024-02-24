def findSquareRootOfNumber(number):
    left = 0
    right = number
    while(left + 1 < right):
        mid = (left + right) // 2
        midS = mid * mid
        if midS == number:
            return mid
        elif midS > number:
            right = mid
        else:
            left = mid
    print(left, right)
    if right * right <= number:
        return right
    else:
        return left
    pass


def main():
 
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(26)))
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(17)))
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(10)))
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(5)))
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(3)))
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(2)))
  print("findSquareRootOfNumber is ---> " + str(findSquareRootOfNumber(100)))


if __name__ == "__main__":
    main()
