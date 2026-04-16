nums = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for x in nums:
    if x not in unique_list:
        unique_list.append(x)

print("Original List:", nums)
print("After Removing Duplicates:", unique_list)
