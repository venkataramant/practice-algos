import sys

# memory
#  findout min of all coinns by deducting coin value

class Solution:
    def coinChange(self, coins, amount):
        coins = sorted(coins)
        print(coins)
        minCoins = [-1]*(amount+1)
        for tempAmount in range(amount+1):
            self.calculateMinCoins(
                coins, tempAmount, tempAmount, minCoins)
        return minCoins[amount]

    def calculateMinCoins(self, coins, cIndex, tempAmount, minCoins):
        if tempAmount == 0:
            minCoins[cIndex] = 0
        else:
            currentMin = -1
            for coin in coins:
                if coin > tempAmount:
                    break
                else:
                    tempMin = -1
                    if minCoins[tempAmount-coin] != -1:
                        tempMin = minCoins[tempAmount-coin]+1
                    if tempMin != -1:
                        if currentMin == -1:
                            currentMin = tempMin
                        else:
                            currentMin = min(currentMin, tempMin)

            minCoins[cIndex] = currentMin


if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    amount = 6
    coins = [186, 419, 83, 408]
    amount = 6249
    print(" mincoins-->", sol.coinChange(coins, amount))
