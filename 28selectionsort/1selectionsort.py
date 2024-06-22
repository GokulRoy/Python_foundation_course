def ssort(nums):
    for i in range(len(nums)-1):
        #  print(i)
        min_pos = i
        for j in range(i,len(nums)):
            if nums[j]<nums[min_pos]:
                min_pos = j
        #     print(j,end="")
        # print()
        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp


nums = [5,3,6,7,2,8]
ssort(nums)
print(nums)