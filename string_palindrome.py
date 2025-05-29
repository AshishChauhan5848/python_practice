s = input("Enter a string: ")


# by slicing method
if str == str[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")

# wihout slicing

reverse_s = ""
for char in s:
    reverse_s = char + reverse_s
print(reverse_s)



