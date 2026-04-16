nums = [10, 20, 4, 45, 99, 99]

# 1. Find the absolute biggest number
biggest = max(nums)

# 2. Create a new list without any 99s
remaining_nums = []
for x in nums:
    if x != biggest:
        remaining_nums.append(x)

# 3. The biggest number left is the second largest
second_largest = max(remaining_nums)

print("Second largest element is:", second_largest)
