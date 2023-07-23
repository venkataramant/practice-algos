class Solution:

    def isPalindrome(self, x: int) -> bool:
        new_num = x 
        index = 0
        while(new_num > 10):
            new_num = new_num // 10
            index += 1
            
        return self.verify_plaindrome(x,index)
    
    def verify_plaindrome(self, x, index):
        while(x > 0):
            if x % 10!= x // pow(10, index):
                return False
            print(index, x, x // pow(10, index), x % 10, x // pow(10, index) == x % 10)
            x = x % pow(10, index)
            x = x // 10
            index -= 2
        return True
       
    def isPalindrome2(self, x: int) -> bool:
        new_value = 0
        index = 0
        remaining_value = x
        
        while(remaining_value > 0):
            new_value = new_value * 10 + remaining_value % 10
            remaining_value = remaining_value // 10
        if new_value == x:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    x = 92999
    print(x, " isPalindrome -->", sol.isPalindrome(x))
