#  Second Largest Element of Array 

def second_largest_element(nums):
    largest = float('-inf')
    S_largest = float('-inf')
    for i in range(len(nums)):
        largest = max(largest,nums[i])
    for i in range(len(nums)):
        if nums[i] > S_largest and nums[i] != largest:
            S_largest = nums[i]
    return S_largest 
nums = [1,2,3,5,6,7,99]
print(second_largest_element(nums))