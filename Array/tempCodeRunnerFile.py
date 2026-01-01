
def largest_element(nums):
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        if nums[i] > largest:
            largest = nums
    return largest
nums = [1,2,3,4,5,6,45,9]
print(largest_element(nums))
