from randcrack import RandCrack
from pwn import process, remote

rc = RandCrack()
# proc = process(["python"] + ["chall.py"])

REMOTE_URL = "chals.bitskrieg.in"
REMOTE_PORT = 7007

proc = remote(REMOTE_URL, REMOTE_PORT)

count = 0

print("================= submitting ===============")
for i in range(624):
    count = count + 1
    print(proc.recvuntil(b'>'))
    proc.sendline(b'1')
    res = proc.recvline()
    numbers = [int(s) for s in res.split() if s.isdigit()]
    password = ((int(numbers[0]) + 1) // 2969596945) // (count ^ 195894762 ^ 322420958)
    print(f"[{count}] ", numbers[0] + 1)
    print("[password] ", password)
    rc.submit(password)

print("================= testing ==================")
for i in range(10):
    count = count + 1
    proc.recvuntil(b'>')
    proc.sendline(b'1')
    res = proc.recvline()
    numbers = [int(s) for s in res.split() if s.isdigit()]
    password = (int(numbers[0]) + 1)
    new = rc.predict_getrandbits(32) * ((count ^ 195894762) ^ 322420958) * 2969596945
    print(f"[{count}] Attempt no {count}")
    print("[password] ", password)
    print("[test] ", new)
    if password == int(new):
        print(f"\033[92m[+] Test {i + 1} Passed \033[0m")
    else:
        print(f"\033[91m[-] Test {i + 1} Failed \033[0m")

print("================= attempting ===============")
for i in range(10):
    count = count + 1
    proc.recvuntil(b'>')
    new = rc.predict_getrandbits(32) * ((count ^ 195894762) ^ 322420958) * 2969596945
    print(f"[{count}] Attempt no {count}")
    print("[*] Submitting number ", new)
    proc.sendline(str(new).encode())
    res = proc.recvline()
    if "Granted" in res.decode().strip():
        print("\033[95m[+] ", res.decode().strip(), "\033[0m")
        break
    else:
        print(f"\033[91m[-] Attempt {i + 1} Failed \033[0m")




proc.close()

