s = input("Enter a string: ")

vowels = "aeiou"

s= s.lower()
count=0
for char in s:
    if char in vowels:
        count+=1

print("no of vowels : ", count) 