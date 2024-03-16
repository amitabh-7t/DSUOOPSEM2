def is_prime(n):
    """Function to check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def print_prime_numbers_up_to(num):
    """Function to print prime numbers up to a given number."""
    print("Prime numbers up to", num, "are:")
    n = 2
    while n <= num:
        if is_prime(n):
            print(n)
        n += 1

# Get user input for the number
num = int(input("Enter the number: "))
# Call the function to print prime numbers up to the given number
print_prime_numbers_up_to(num)
