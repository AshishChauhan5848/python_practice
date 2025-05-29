num = input("Enter a number: ")

freq={}

for char in num:
    freq[char]= freq.get(char,0)+1

print("character frequency" , freq)