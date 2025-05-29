# # without function
num = int(input("enter a number: "))

factorail =1
if (num==0 or num==1):
    print(num)
for i in range (1,num+1):
    factorail *=i
print(factorail)

# with function

def factorial(n):
    fact=1
    if (num==0 or num==1):
        return 1
    else:
        for i in range (1,num+1):
            fact*=i
        return fact
    
    
num = int(input("enter a number: "))
print("factorial",factorial(num))


# with recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
num = int(input("enter a number: "))
print("factorial",factorial(num))