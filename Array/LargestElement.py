# Largest Element Of Array In DSA

#  First Step 

# numbers = [1,5,9,2,34,56,3]
# largest = max(numbers)
# print(f"The largest element of array:",largest)

#  Second Method

# numbers = [1,5,9,23,4,55,69,8]
# if not numbers:
#     print("Its is not a largest numbers:")
# else:
#     largest = numbers[0]
#     for num in numbers[1:]:
#         if num > largest:
#             largest = num
#     print(f"Largest element hai {largest} ")

# cook your dish here
def largest_number(nums):
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        if nums[i] > largest:
            largest = nums[i]
        # largest = max(largest,nums[i])
    return largest 
nums = [1,2,5,7,9,34,22,98]
print(largest_number(nums))