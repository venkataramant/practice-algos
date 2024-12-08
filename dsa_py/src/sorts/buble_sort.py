from typing import List

# Each Iteration select minimum value from unsorted array(second half) append to sorted array(first half)
# After K th iteration, first K elements are in sorted  order.
def selectionSort(arr: List[int]) -> None: 
    for index in range(len(arr)):
        minIndex = index
        for index2 in range(index, len(arr)):
           if arr[index2] < arr[minIndex]:
               minIndex = index2
        arr[index], arr[minIndex] = arr[minIndex], arr[index]
        print(arr[:index+1])
        # tValue = arr[index]
        # arr[index] = arr[minIndex]
        # arr[minIndex] = tValue
    return arr


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 10, 6, 3, -8, 2]
    result = selectionSort(nums)
    print(nums, "-->", result)
