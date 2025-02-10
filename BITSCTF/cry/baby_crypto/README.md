# Baby Crypto

Points: 50

> I do not think it gets easier than this...

---

We were a given an RSA Oracle, which is a pretty comman an easy crypto challenge. An Oracle in cryptography is something that
will decipher any encrypted message you give it, except the main ciphertext itself. So it's output will look something like

```
n = (very large public key)
e = 65537 or something idr
c = the ciphertext

enter cipher text to decode
> ...
```

let's refresh how RSA encryption works

our ciphertext is simply

$$
c = m^{e} \mod{n}
$$

where $m$ is the plaintext

To decrypt this we need our private key 

$$
d = e^{-1} \mod{(p-1)(q-1)}
$$

and our message is deciphered as 

$$
m = c^{d} \mod{n}
$$

now what if we multiplied $c$ with $2^{e}$ and passed that into the oracle instead? When it's decrypted we get
essentially $2 * m$ which we can divide by 2 to get $m$, which is our flag

I'm not very clear with modular arithmetic, so here's a better resource. [Cool StackExchange Answer](https://crypto.stackexchange.com/questions/2323/how-does-a-chosen-plaintext-attack-on-rsa-work/2331#2331)

```py
from Crypto.Util.number import long_to_bytes

print(long_to_bytes(39639837536156593072703000049994066086289431135207913625429785307924943603979635946981909260898213168370823268973219279443746657679296399190096606077830951260950823052936192667655676091351812437731066 // 2))
```

---

```sh
BITSCTF{r54_0r4acl3_h4s_g0t_t0_b3_0n3_0f_7h3_3as13st_crypt0_1n_my_0p1n10n_74b15203}
```
