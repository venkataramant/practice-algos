from typing import List
import heapq
class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        min_heap = []
        max_heap = []
        heap_size = k % 2 + (k // 2)
        for x in range(k):
            heapq.heappush(min_heap, nums[x])
            heapq.heappush(max_heap, -nums[x])
            if len(min_heap) > heap_size:
                heapq.heappop(min_heap)
            if len(max_heap) > heap_size:
                heapq.heappop(max_heap)
        print(max_heap, min_heap)
        min_v = min_heap[0]
        max_v = -max_heap[0]
        ans.append((min_v + max_v) / 2)
        last_index = 0
        for x in range(k, len(nums)):
            heapq.heappush(min_heap, nums[x])
            heapq.heappush(max_heap, -nums[x])
            print("Delete", nums[last_index])
            if nums[last_index] in min_heap:
                min_heap.remove(nums[last_index])
                heapq.heapify(min_heap)
            if -nums[last_index] in max_heap:
                max_heap.remove(-nums[last_index])
                heapq.heapify(max_heap)
            if len(max_heap) > len(min_heap):
                extra = heapq.heappop(max_heap)
                heapq.heappush(min_heap, extra)
            elif len(max_heap) < len(min_heap):
                extra = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -extra)
                
            last_index += 1
            print(max_heap, min_heap)
            print(-max_heap[0], min_heap[0])
            min_v = min_heap[0]
            max_v = -max_heap[0]
            ans.append((min_v + max_v) / 2)
        
        return ans

            
if __name__ == "__main__":
    sol = Solution()
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    ans = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
    # nums = [8,6,6,4,2,1, 3, -1, -3, 5, 3, 6, 7]
    print(nums, " longestAlternatingSubarray-->", sol.medianSlidingWindow(nums, k) == ans)
