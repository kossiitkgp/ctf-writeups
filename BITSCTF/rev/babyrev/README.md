# Baby Rev

Points: 50

Solves: 233

---

In the `chall.py` we notice 

```py
# Python obfuscation by freecodingtools.org
```

Which shows me that they used [this](https://freecodingtools.org/tools/obfuscator/python) to obfuscate the challenge program.

I was sure other people would have created a script to reverse this since the obfuscation didn't look too strong, just repetitive, and that led me to find [freedcodingtools-python-deobfuscator](https://github.com/a2heus/freecodingtools-python-deobfuscator/tree/main) by [a2heus](https://github.com/a2heus)

I used the provided `decompress.py` script to get the flag

```py
# Online Python Compiler

print("Hello, World!")
# BITSCTF{obfuscation_and_then_some_more_obfuscation_4a4a4a4a}
```

---

```sh
BITSCTF{obfuscation_and_then_some_more_obfuscation_4a4a4a4a}
```
