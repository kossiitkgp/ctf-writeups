# Baby DFIR

Points: 50

> I promise this is actually easy.

---

We were given an `.ad1` image that you had to analyse. It contained a `flag.txt` that gave you the flag.

Very simple, why am I writing a writeup then?

Because `.ad1` is a proprietary image format from what I remember and you need to use FTK Image on windows to analyse it.

Now I don't have Windows. (I use arch btw). I had previously missed out on forensics challenges because I couldn't get FTK Imager to work on my setup, and it wasn't working this time either. 

Thankfully I found a fantastic new tool :DDDD

[AD1-tools](https://github.com/al3ks1s/AD1-tools?tab=readme-ov-file) by [al3ks1s](https://github.com/al3ks1s) is absolutely amazing. I had some trouble setting it up intially, but then I just downloaded the release instead of cloning the repo and ran the set up scripts.

```sh
tar -xf ad1tools-1.0.tar.gz
cd ad1tools-1/
./configure
cd AD1-tools/
sudo make
```

now I can choose either to mount the `.ad1` or extract it. Let's extract it.

```sh
❯ ad1extract -i abc.ad1 --output-dir ./extract/ --metadata --verbose
Extracting files
Finished extracting⏎     

❯ ll ./extract/
total 8.0K
-rw-r--r-- 1 subzcuber subzcuber 282 Feb  6 22:20 desktop.ini
-rw-r--r-- 1 subzcuber subzcuber  47 Feb  6 22:51 flag.txt

❯ cat ./extract/flag.txt 
BITSCTF{a_really_simple_intro_to_DFIR_12848a9e}   
```

gg ez

---

```sh
BITSCTF{a_really_simple_intro_to_DFIR_12848a9e}
```
