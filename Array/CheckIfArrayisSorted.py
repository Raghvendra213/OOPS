# Check if array is sorted 

def array_sorted(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True
nums = [1, 2, 3, 4, 5]
print(array_sorted(nums))