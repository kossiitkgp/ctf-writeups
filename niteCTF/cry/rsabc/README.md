# RSAabc

Points: 50

__crypto__

> A blend of encryption methods hides the answer. You might flip out a bit but don't worry, can you crack the code?

Author: Snapskillz

---

We are given the `cipher.py` file and `out.txt`

`cipher.py` has a bunch of helper functions defined
```python
def googly(number, position):
def string_to_int(message):
def int_to_string(number):
def rsa_encrypt(message, public_key):
def reverse_alphabet(char):
```

What `reverse_alphabet` is doing is converting `a` -> `z`, `b` -> `y` and so on. Same for capital letters. If it encounters `{}_` then it replaces them with `e`

now for each character in the flag, if the characters ascii is
- **Not Prime**: 
    - first reverse the character and put it in `out.txt`
    - then get its `ascii value % 26` and gen a prime no. of that value + 5 bits.
    - This is the `p` value of our rsa encrypt
    - then it does a standard rsa_encryption
    - This is easy to decipher in dcode, because the p value is pretty small

    > out: `mrgπeτfΟΔςoΝeηiδyegsλexlwVαehιΠπμZe`
    >
    > on reversing this gives
    >
    > `nit-{-u---l-_-r-b_th-_codE-_s----A}` where the blanks are to be filled with characters with prime ascii values

- **Prime**:
    - first thing the code does is get a number based on the ciphertext of the character. 
    - Then based on that number it gets a greek character from the defined dictionary
    - then xors the ciphertext using the `googly()` function at the position given by the greek character. Thankfully it writes the greek character to `out.txt`
    - to reverse this we just need to xor it again and we can then decode the ciphertext in dcode
    - I did this manually for every single character until the flag was reconstructed

If anyone reads this please tell me a better way to have done this. I tried generating a list of all the prime values that p could have taken, however that looked like it was far too big to be useful

```
flag: nite{quICklY_grab_the_codE5_sgOqkA}
```

---

The reason I didn't think I would be able to write a script was because 
I didn't know we could find prime factors in python. Updated with new script
