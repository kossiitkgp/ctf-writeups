# Finders Keepers

Points: 108

> What even is this image bruh.

`Author: darthlazius@13`

---

Binwalk on the `weird.png` gave me the `image.jpg`

```sh
binwalk -ave weird.png
```

I simply uploaded the image to [AperiSolve](https://www.aperisolve.com/) and a bunch of other people
had the same idea so the stego password was already uploaded there. 

password: `snooooooppppppp`

then just

```sh
❯ steghide extract -sf image.jpg
Enter passphrase: snooooooppppppp
wrote extracted data to "flag.txt".
```

I doubt this is the intended solve though. 

Going through discord, apparently there was a `.wav` in the image too which binwalk didn't extract idk why

You can extract it with `foremost`. The `.wav` contained morse that apparently gave us our steg password "snooooooppppppp"

```sh
foremost weird.png
```

---

```sh
BITSCTF{1_4m_5l33py_1256AE76}
```
