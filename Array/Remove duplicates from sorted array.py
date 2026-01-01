# Remove duplicates from sorted array

def remove_element(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0,n):
        freq_map[nums[i]] = 0
    j = 0
    for k in freq_map:
        nums[j] = k
        j+=1
    return j
nums = [1,1,1,2,3,4,4,4,5,6,7,8]
print(remove_element(nums))

#  Optimal Solution 

