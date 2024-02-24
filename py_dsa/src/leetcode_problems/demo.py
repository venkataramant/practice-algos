class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        subStringLen = k
        kBeautity = 0
        tempNum = num 
        while(tempNum >= pow(10, k-1)):
            print("tempNum ",tempNum)
            subInt = (tempNum ) % (pow(10, k))
            if subInt != 0 and num % subInt == 0:
                print("subInt ",subInt)
                kBeautity += 1
            tempNum=tempNum // 10
                        
        return kBeautity

if __name__ == "__main__":
    sol = Solution()
    num = 430043
    k = 2
    kBeautity=sol.divisorSubstrings(num, k)
    print("kBeautity",kBeautity)
