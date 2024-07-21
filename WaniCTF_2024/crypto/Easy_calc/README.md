# Easy_calc

description:

> 😆

## Approach

> !! **We weren't able to solve this during the CTF** !!

so basically the encryption algorithm is using an AES cipher using `s` as the key, and given `p` and `A` we have to get the value of `s`

```py
u = 0
    for i in range(p):
        u += p - i
        u *= s
        u %= p
```

this is the algorithm used to generate `A` that we have to crack

taking some dry runs:
$$
u = s(p-1) \mod p \newline
u = s(p - s - 2) \mod p \newline
u = s(p - s^2 - 2s - 3) \mod p \newline
$$
and so on

this gives us something like the series
$\sum\_{i=1}^{p-1} is^{p-i} \mod p$ which is an AGP

solving this AGP gave me
$$

\frac {s(s^p - s)}{(s-1)^2} - \frac {s(p-1)}{(s-1)}\mod p
$$

at this point I was stumped because I had no idea how to solve for $s$ with the $s^p$ term in the expression, I remembered seeing a considerably simpler expression in the WaniCTF discord which motivated me to try further

I searched for

> $s^p \mod p$

and was guided to ["Fermat's Little Theorem"](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem) which states that
$$
s^p - s \mod p = 0
$$
this means that I can neglect the first term in my AGP expression giving me finally
$$
A = \frac {s}{(1-s)} \mod p
$$
which I can rearrange for s as
$$
s = \frac {A}{A + 1} \mod p
$$

now I have $A, p$ which gives me $s$ and I also have the `iv`, now I can decrypt the AES cipher

I still stumbled with the python code and took help from some writeups though

## Flag

Flag: `FLAG{Do_the_math396691ba7d7270a}`