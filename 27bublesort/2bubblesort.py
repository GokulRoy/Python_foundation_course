def sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
        # this is used to print nums after every iteration
        print(nums)
        #     print(j,end="")
        # print()
        
nums = [5,3,8,6,7,2]
sort(nums)
print(nums)