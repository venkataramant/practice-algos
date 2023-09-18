class Solution:

    def isPalindrome(self, s: str) -> bool:
        print(s)
        if len(s) == 1 or len(s) == 0:
            return True
        if s[0] == s[len(s) - 1]:
            return self.isPalindrome(s[1:len(s) - 1])
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    s = "99999"
    print(s, " isPalindrome -->", sol.isPalindrome(s))
