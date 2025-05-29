for num in range(2, 101):
    is_prime = True  # Assume num is prime initially
    for i in range(2, int(num ** 0.5) + 1):  # Check up to square root of num
        if num % i == 0:
            is_prime = False  # Found a divisor
            break
    if is_prime:
        print(num, "is a prime number")