# beginners_aes

description:

> AES is one of the most important encryption methods in our daily lives.

## Approach

this challenge was solved by [@harshkhandeparkar](https://github.com/harshkhandeparkar)

he told me to give it a try so I'm doing that now (a month after the ctf)

the main expoit is that the key and iv are both almost given to us save for 1 byte

this gives us 128\*128 possible combinations which is easily brute forceable

You can see the entire solution in `solve.py`

## Flag

Flag: `FLAG{7h3_f1r57_5t3p_t0_Crypt0!!}`
