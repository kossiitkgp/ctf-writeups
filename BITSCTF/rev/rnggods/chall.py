import random
import os
import dis

# Generate a random seed from 8 bytes of random data
seed = int.from_bytes(os.urandom(8), "big")
random.seed(seed)

flag = "REDACTED"  # Hidden flag value

def generate_password(i):
    return (random.getrandbits(32) * ((i ^ 195894762) ^ 322420958) * 2969596945)
    # return (random.getrandbits(32) ^ 195894762 ^ 322420958) % 2969596945

print("Vault is locked! Enter the password to unlock.")

i = 1  # Iteration counter

print(dis.dis(generate_password))

while True:
    password = generate_password(i)
    attempt = input("> ")
    
    if not attempt.isdigit():
        print("Invalid input! Enter a number.")
        continue
    
    difference = abs(password - int(attempt))
    
    if difference == 0:
        print("Access Granted! Here is your flag:", flag)
        break
    else:
        print(f"Access Denied! You are {difference} away from the correct password. Try again!")
        i += 1

