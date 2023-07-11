class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        strInt = str(num)
        strIntLen = len(strInt)
        subStringLen = k
        kBeautity = 0
        previousIndex=0
        while(previousIndex+subStringLen  <= strIntLen):
            subStr = strInt[previousIndex:previousIndex + subStringLen]
            print("subStr",subStr)
            if subStr!=None and subStr!="" and int(subStr)!=0 and num % int(subStr) == 0:
                
                kBeautity += 1
            previousIndex += 1 

                        
        return kBeautity
