def sieve_of_eratosthenes(max_num):
    """Generate a list of prime numbers up to max_num using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_num + 1)
    p = 2
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    return [num for num, prime in enumerate(is_prime) if prime]

# Define the range for 5 bits to 30 bits
min_bits = 5
max_bits = 30
max_num = (1 << max_bits) - 1  # 2^30 - 1

# Generate primes
primes = sieve_of_eratosthenes(max_num)

# Filter primes to only include those from 5 bits to 30 bits
filtered_primes = [p for p in primes if p >= (1 << (min_bits - 1))]

# Print the primes in a comma-separated list
print(', '.join(map(str, filtered_primes)))
