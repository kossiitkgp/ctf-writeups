# Surveillance of Sus

```
rating: Normal
points: 126pt
```

description:

> A PC is showing suspicious activity, possibly controlled by a malicious individual.
>
> It seems a cache file from this PC has been retrieved. Please investigate it!

## Approach

In this challenge we were given the `Cache_chal.bin` file. For a very long time I thought this challenge
was about memory dumps, so I went ahead with struggling to setup `volatility3`. However when that didn't
work I finally turned to other approaches.

I finally searched up what a `.bin` file even is and it was simply a file of binary data. I remembered
that files often have a header for their data type, so I ran

```
strings Cache_chal.bin
```

this gave me

```
[subzcuber@hpelitebook] :) {1012}$ strings Cache_chal.bin
RDP8bmp
i2\@
kaSDr@
:kQ@
{b`R
.Nw@
*kj: # and more ...
```

We can immediately notice the `RDP8bmp` at the top. I ddged this. That told me that I can install a tool
called `bmc-tools` to extract the information. I did this and got the flag.

However before I share the flag I would like to share a bit more about RDP and bitmaps and caches since
I didn't read any of this during the CTF itself.

**RDP** stands for *Remote Desktop Protocol*. It is a protocol created by Microsoft to allow users to
connect to a remote desktop. RDP8 is simply Version 8.0 of RDP.

A **bitmap** is just an image, a literal map of bits arranged to give you a digital image. Many GUIs
use bitmaps for their graphics, namely Microsoft.

Now the part where cache comes in is that when sharing data via `RDP` you can cache bitmap images to
reduce the load on the connection, and what we have been given is one such cache file.

Going back to `bmc-tools`. I installed it with

```
git clone https://github.com/ANSSI-FR/bmc-tools.git
```

then ran

```
python ./bmc-tools/bmc-tools.py -s Cache_chal.bin -d . -b
```

this made a collage of the 650 different bitmap images into one

## Flag

the collage:

![](./Cache_chal.bin_collage.bmp)

FLAG: `FLAG{RDP_is_useful_yipeee}`
