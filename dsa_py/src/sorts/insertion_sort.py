from typing import List

# In kth iteration, insert kth element(first element from unsorted-part) into sorted part[0 to k-th array]
# After K the iteration , K elements from last are in sorted manner


def insertSort(arr: List[int]) -> None: 
    for index in range(1,len(arr)):
        correctIndex=0
        for index2 in range(0,index):
           if arr[index2] < arr[index]:
               continue
           else:
               
               arr[index2] , arr[index2 + 1] = arr[index2 + 1], arr[index2]
        # print(arr[-1*(index+1):])
    return arr


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 10, 6, 3, -8, 2]
    result = selectionSort(nums)
    print(nums, "-->", result)
