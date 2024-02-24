from typing import List

# Each Iteration  compare adjacent numbers and sort them
# After K the iteration , K elements from last are in sorted manner


def selectionSort(arr: List[int]) -> None: 
    for index in range(len(arr)):
        for index2 in range(0, len(arr) - index - 1):
           if arr[index2] > arr[index2 + 1]:
               arr[index2] , arr[index2 + 1] = arr[index2 + 1], arr[index2]
        # print(arr[-1*(index+1):])
    return arr


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 10, 6, 3, -8, 2]
    result = selectionSort(nums)
    print(nums, "-->", result)
