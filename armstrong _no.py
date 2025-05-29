num = int(input("Enter a number: "))

temp =num
sum=0
order= len(str(num))

while temp>0:
    digit = temp%10
    sum = sum + digit ** order
    temp//=10

if num == sum:
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")
