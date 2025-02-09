from pwn import process
import string

for i in string.printable:
    payload = f"BITSCTF\x7bC4ND4C3_L0G1C_W0RK{i}"
    proc = process(["./loginator.out"] + [payload])
    res = proc.recvline().decode().strip()
    print(f"[{i}] trying string {payload}")
    if res == "02 92 a8 06 77 a8 32 3f 15 68 c9 77 de 86 99 7d 08 60 8e 64 77 be ba 74 26 96 e7":
        break
    proc.close()


