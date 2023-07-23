def modify_list(nums, index, multiplier):
    nums[index] *= multiplier
    print(nums)


def verify_list():
    nums = [2, 4, 6, 8]
    for index in range(len(nums)):
        modify_list(nums.copy(), index, index+1)
        


if __name__ == "__main__":
    verify_list()
    
