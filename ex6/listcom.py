print("Convert each character of a string into uppercase")
text1 = "python"
result1 = [char.upper() for char in text1]
print("1. Uppercase:", result1)

print("Extract all vowels from a given string")
text2 = "hello world"
result2 = [char for char in text2 if char.lower() in 'aeiou']
print("2. Vowels:", result2)

print("Remove all negative numbers from a list")
nums3 = [10, -5, 20, -3, 0]
result3 = [num for num in nums3 if num >= 0]
print("3. No negatives:", result3)

print("Replace all negative numbers in a list with 0")
nums4 = [10, -5, 20, -3, 0]
result4 = [num if num >= 0 else 0 for num in nums4]
print("4. Replaced with 0:", result4)

print("Create a list of cubes of numbers from 1 to 10")
result5 = [x**3 for x in range(1, 11)]
print("5. Cubes (1-10):", result5)

print("Create a list containing the first letter of each word in a sentence")
sentence6 = "Learning Python is fun"
result6 = [word[0] for word in sentence6.split()]
print("6. First letters:", result6)

print("Create a list of lengths of each character in a string")
text7 = "code"
result7 = [len(char) for char in text7]
print("7. Character lengths:", result7)

print("Create a list of numbers greater than the average of the given list")
nums8 = [10, 20, 30, 40, 50]
avg = sum(nums8) / len(nums8)
result8 = [num for num in nums8 if num > avg]
print("8. Greater than average:", result8)
