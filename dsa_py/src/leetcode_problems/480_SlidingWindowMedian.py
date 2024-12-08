from typing import List
import heapq
class Solution:

    def medianSlidingWindow(self, nums: List[int], K: int) -> List[float]:
        ans = []
        second_half = []
        first_half = []
        eliminate_index=-1
        for x in range(len(nums)):
            if eliminate_index>=0:
                print("R:" ,x,eliminate_index,-first_half[0],first_half,second_half)
                if nums[eliminate_index]>=first_half[0]:
                    first_half.remove(-nums[eliminate_index])
                else:
                    second_half.remove(nums[eliminate_index])
            heapq.heappush(first_half, -nums[x])
            if len(first_half)-len(second_half)>1:
                heapq.heappush(second_half, -heapq.heappop(first_half))
            
            if len(first_half)+len(second_half)==K:
                eliminate_index+=1
                if K%2==0:
                    ans.append((-first_half[0] + second_half[0]) / 2.0)
                else:
                    ans.append(-first_half[0]/1.0)
                print(ans,eliminate_index)
            
        
        return ans

            
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    K = 3
    ans = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
    # nums = [8,6,6,4,2,1, 3, -1, -3, 5, 3, 6, 7]
    print(nums, " longestAlternatingSubarray-->", sol.medianSlidingWindow(nums, K) == ans)
