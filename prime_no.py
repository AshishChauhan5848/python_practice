num = int(input("Enter a number: "))

if num < 2:
    print(num, "is not a prime number")
else:
    flag = False
    for i in range(2, int(num ** 0.5) + 1):  # Optimization: check up to square root of num
        if num % i == 0:
            flag = True
            break
    if not flag:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


        