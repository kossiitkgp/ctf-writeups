# Biscuits

Points: 50

> Momma, can I have cookie..?
> 
> No....

`Author: d4y0n3`

---

This challenge took me a really long time. Probably close to 5-6 hours for what should be a really easy challenge.

I didn't even decompile it for a long while. 

I had first run it like a 100 times really fast to see all the different cookies requested, and everytime the cookie it wanted was the same, so I thought "Hey, maybe if I send input fast enough, all the 100 cookies it wants will be the same!"

After this came a lot of mucking about with `pwntools` where I first tried to extract all the different cookies, make a set, then bruteforce sending a cookie a 100 times because I thought if I did that fast enough, all 100 requested cookies will be the same. 

Once I finally got a working script, I realised this was not the case and my approach was wrong, so I finally decompiled the binary. 

So what the binary was actually doing was seeding with `srand(time(0))`, then using the value of `(random() % 100) * 8` to dereference a `char*` pointer stored in an array of a 100 such pointers. 

A solution to break this randomness is to just seed with time on your own computer, then both seeds will be almost the same and you just hope that `%` takes cares of the rest. 

First I had to extract the cookies names manually (yes) from the binary in the correct order using `gdb`. Once I had those, I recreated the binary in `solve.c` and passed the output of that into the function.

```sh
./solve | ./main
```

Clearly this will work, however when I tried the same with the actual server, it didn't work. Eventually I figured this was due to some inherent delay in connecting to the server so I used a really hacky solution to this in bash. In `solve.c` I used cli arguments to increase the seed slightly as `srand(time(0) + i)` and passed that `i` with bash in a loop

```bash
$ for i in {0..500};do ./solve $i | nc 20.244.40.210 6000 ; done
```

and somewhere in the middle of this output, one of those values works and I get the flag.

```sh
...
Guess the cookie: Correct! The cookie was: Speculoos
Guess the cookie: Correct! The cookie was: Peanut Butter
Guess the cookie: Correct! The cookie was: Pinwheel Cookie
Guess the cookie: Correct! The cookie was: Gingerbread
Guess the cookie: Correct! The cookie was: Shortcake
Guess the cookie: Correct! The cookie was: Palmier
Congrats!
Flag: BITSCTF{7h4nk5_f0r_4ll_0f_th3_c00ki3s_1_r34lly_enjoy3d_th3m_d31fa51e}
```

As I was writing this I realised I could have simply used the main binary itself and parsed its output instead of manually getting the name of each cookie (ಥ﹏ಥ)

Though I supposed I wouldn't have been able to do my bash thingy in that case and been even more frustrated

> I'm so stupid. I could have just done `strings main` to get the cookie names, instead I went manually to every pointer and printed its value (;´༎ຶД༎ຶ`)
> I was literally doing something like
```gdb
gef➤  x/s (char**)(cookies)
0x555555557008:	"Chocolate Chip"
```
> individually for each cookie

---

```sh
BITSCTF{7h4nk5_f0r_4ll_0f_th3_c00ki3s_1_r34lly_enjoy3d_th3m_d31fa51e}
```
