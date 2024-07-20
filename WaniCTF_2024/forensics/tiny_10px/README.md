# tiny_10px

description:

> What a small world!

## Approach

> !! **I wasn't able to solve this challenge during the CTF** !!

For this challenge we were given the `.jpg` image

![](./chal_tiny_10px.jpg)

Opening the image in GIMP throughs the following error

> Corrupt JPEG data: 41231 extraneous bytes before marker 0xd9

The only interesting info I found in the exiftool info was

```
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches

Displayed Units X               : inches
Displayed Units Y               : inches
Image Width                     : 10
Image Height                    : 10
```

and binwalk didn't reveal anything obvious to me either

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, EXIF standard
12            0xC             TIFF image data, big-endian, offset of first image directory: 8
483           0x1E3           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
```

## Solution

After the ctf I saw on the WaniCTF discord that the given image was only being displayed partly and the rest was hidden

This still didn't give me an obvious solution so I went looking for the writeups. The most helpful one was [definintely this one](https://warlocksmurf.github.io/posts/wanictf2024/)

In this writeup the author links to this amazing reference for [hiding info by manipulating an image's height](https://cyberhacktics.com/hiding-information-by-changing-an-images-height/)

following the instructions in the article, I converted my image to hex in cyberchef, found the `ff c0` marker identifier and messed around with height and width until I could see the full image :)

## Flag

![](./solved_tiny_10px.jpg)

FLAG: `FLAG{b1g_en0ugh}`
