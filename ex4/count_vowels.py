count = 0
vowels = 'aeiouAEIOU'

s=input("Enter a string")
for c in s:
    if c in vowels:
        count+=1

print("No.of Vowels are : ",count)
