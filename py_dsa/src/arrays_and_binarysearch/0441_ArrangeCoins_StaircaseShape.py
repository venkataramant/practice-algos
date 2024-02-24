def arrangeCoins(n):
    left = 0
    right = n
    while(left + 1 < right):
          mid = (left + right) // 2
          total_coins = (mid * (mid + 1)) // 2
          if total_coins == n:
              return mid
          elif total_coins < n:
              left = mid
          else:
              right = mid
    print(left, right)
    if left!=0:
        return left
    else:
        return right
          
    return -1


def main():
 
  # print("arrangeCoins is ---> " + str(arrangeCoins(5)))
  # print("arrangeCoins is ---> " + str(arrangeCoins(8)))
  print("arrangeCoins is ---> " + str(arrangeCoins(1)))
  print("arrangeCoins is ---> " + str(arrangeCoins(0)))
  # print("arrangeCoins is ---> " + str(arrangeCoins(5)))
  # print("arrangeCoins is ---> " + str(arrangeCoins(3)))
  # print("arrangeCoins is ---> " + str(arrangeCoins(2)))
  # print("arrangeCoins is ---> " + str(arrangeCoins(100)))


if __name__ == "__main__":
    main()
