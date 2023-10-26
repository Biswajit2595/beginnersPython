def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    if number <= 3:
        return True  # 2 and 3 are prime

    if number % 2 == 0 or number % 3 == 0:
        return False  # Divisible by 2 or 3

    i = 5
    while i * i <= number:
        if number % i == 0:
            return False  # Divisible by i or i+2
        i += 6

    return True

# Example usage:
number = 4
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
