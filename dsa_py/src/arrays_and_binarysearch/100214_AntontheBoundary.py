from typing import List
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        if not nums and len(nums)==0:
            return 0
        ans=0
        
        queue=[nums[0]]
        for num in nums[1:]:
            print(num,queue)
            if len(queue)==0:
                queue.append(num)
                continue
            if (num>0 and queue[len(queue)-1]<0):
                sum1=None
                while(len(queue)>0 and queue[len(queue)-1]<0):
                    num=num+queue.pop()
                    if num<0:
                        queue.append(num) # it cross the boundary append to it
                        break
                if num>0:
                    queue.append(num)
                elif num==0:
                    ans+=1
                print(num,queue)
            elif (num<0 and queue[len(queue)-1]>0):
                print(num,queue)
                while(len(queue)>0 and queue[len(queue)-1]>0):
                    num=num+queue.pop()
                    if num>0:
                        queue.append(num) # it cross the boundary append to it
                        break

                if num<0:
                    queue.append(num)
                elif num==0:
                    ans+=1
                print(num,queue)
            else:
                # last one and current one in same direction
                queue.append(num)
        print(queue)
        return ans




if __name__ == '__main__':


    arr = [-4,8,-4,2]
    ans=1
    arr = [3,2,-3,-4]
    ans=0
    arr = [-9,2,-10,10]
    ans=0
    obj = Solution()
    result = obj.returnToBoundaryCount(arr)
    
    print(result,ans,ans==result)
    

