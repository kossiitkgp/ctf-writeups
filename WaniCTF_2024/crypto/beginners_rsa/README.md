# beginners_rsa

```
rating: beginner
points: 121pt 
```

description:

> Do you know RSA?

## Approach

We are given the encryption source code `chall.py` and the message to decode `output.txt`

First we had to learn what RSA is.

RSA is a cipher named after its creators. One of problems in cryptogrphy is the necessity of having to
share the key with someone so that they can decrypt your message. Public key ciphers like RSA can be encrypted by
anyone, but decrypted only by those with the private key, so it is no longer a *necessity* for the encrypter to
have to share a key with the receiver.

The way typical RSA works is that two very large and random prime numbers are generated

these are our $p$ and $q$

we can work with PyCrypto library which can be installed on Arch with

```
sudo pacman -S python-pycrptodome
```

```
from Crypto.Util.number import *

p = getPrime(1024)
q = getPrime(1024)
```

using $p$ and $q$ as our prime factors we get

```
n = p*q
```

and an encryption key is used typically

```
e = 0x10001 # 65537
```

now we start encrypting our message

```
FLAG = b'FLAG{This_is_a_fake_flag}' # this is our plaintext
m = bytes_to_long(FLAG)
enc = pow(m, e, n) # this is our encrypted ciphertext
```

What is that `pow()` function doing

What that does is return
$$enc = (m^e)\\mod n$$

Now we come to the decryption

The minimum required information to decrypt RSA is the value of $n, e, m$ and either one of $p$
or $q$

From those you would calculate

```
w = (p-1)*(q-1)
```

and find the private key as

```
d = inverse(e, w)
```

What `inverse()` does is return the modular multiplicative inverse i.e.
$$d = e^{-1}\\mod w$$
and the decrypted key is given by

```
dec = pow(enc, d, n)
```

or
$$dec=(enc^d)\\mod n$$

Now coming to actual challenge

In `chall.py` notice two things, first that there are 5 prime factors being used instead of 2,
and second that the prime factors are only 8 bytes instead of 128.

> I noticed that the factors are small because when I plugged the values into [dCode.fr](https://www.dcode.fr/chiffre-rsa)
> I was told that `n` is small so I could brute force the prime factor decomposition

my first approach was to simply put

```
w = (p-1)*(q-1)*(r-1)*(a-1)*(s-1)
```

and proceed as normal. This was in fact the correct solution. However I wasn't good enough at python to
be confident that `dec` was in fact = `m` and I was pretty sure that wouldn't work anyway, so I went ahead
with my next approach which was to follow [this StackOverflow question](https://crypto.stackexchange.com/questions/31109/rsa-encryption-and-decryption-with-multiple-prime-modulus-using-crt)

[@harshkhandeparkar](https://github.com/harshkhandeparkar) and I were discussing this one closely,
I managed to understand the algorithm with his help. It was an implementation of the Chinese Remainder
Theorem, which seems easy when you think about it, but quite complex when you write it in modular arithmetic

Eventually I did manage to implement the algorithm in python and get the given example to match, however
when I tried to replicate that in the `./chall.py` script it didn't match. Eventually I gave up and went to sleep.

In the morning I woke up fresher and managed to get my first idea to work which you can see in `./solve.py` :)

If anyone finds the mistake I made in the 2nd approach, please let me know

## Flag

FLAG: `FLAG{S0_3a5y_1254!!}`
