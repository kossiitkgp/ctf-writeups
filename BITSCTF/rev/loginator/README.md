# Loginator

Points: 50

Solves: 153

> `02 92 a8 06 77 a8 32 3f 15 68 c9 77 de 86 99 7d 08 60 8e 64 77 be ba 74 26 96 e7`

---

We are given a binary that obfuscates some text. Giving it `BITSCTF` returned 

```console
❯ ./loginator.out BITSCTF
02 92 a8 06 77 a8 32
```

which matches the first few bytes of the description. This now turns into a bruteforcing problem

With the help of my solve script I manually got each character and recreated the flag, letter by letter. (there's probably a better way to do this, but don't look at me, idk python)

```python
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
```

I had to escape that first `{` with `\x7b` for some reason, I'm not sure what was up with that

---

```sh
BITSCTF{C4ND4C3_L0G1C_W0RK}
```
