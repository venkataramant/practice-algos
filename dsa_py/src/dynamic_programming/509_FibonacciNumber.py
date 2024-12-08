class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        num1=0
        num2=1
        for x in range(2,n):
            temp=num1+num2
            num1=num2
            num2=temp
            print(x,num1,num2)
        return num1+num2

if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(n, " fib-->", sol.fib(n))
