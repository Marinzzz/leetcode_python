def removeDuplicates():
    nums = [1, 1, 1, 2, 2, 3]
    record = 0
    if len(nums) <= 2:
        return len(nums)
    n = len(nums)
    i = 1
    while i < n:
        if nums[i] == nums[i - 1]:
            record += 1
            if record == 2:
                nums.remove(nums[i])
                n -= 1
                i -= 1
                record -= 1
        else:
            record = 0
        i += 1
    print(nums)
removeDuplicates()
