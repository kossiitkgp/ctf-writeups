# replacement

description:

> No one can read my diary!

## Approach

> This question was first solved by [@harshkhandeparkar](https://github.com/harshkhandeparkar), I tried it during after him and got it too

For this challenge we are given an encryption algorithm and the encrypted text.

We have to notice that every single character in the encrypted text is being hashed, this gives us only around 150-200 unique hashes, which is quite easy to bruteforce against.

So in `solve.py` first we create the db of unique hashes using the `strings.printable` thing in python

then we check against the encrypted text and replace the hashes with the characters

Here is the decrypted diary entry

> ```
> Wednesday, 11/8, clear skies. This morning, I had breakfast at my favorite cafe. Drinking the freshly brewed coffee and savoring the warm buttery toast is the best. Changing the subject, I received an email today with something rather peculiar in it. It contained a mysterious message that said "This is a secret code, so please don't tell anyone. FLAG{13epl4cem3nt}". How strange!
>
> Gureisya
> ```

## Flag

Flag: `FLAG{13epl4cem3nt}`
