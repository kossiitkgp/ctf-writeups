# BackdoorCTF 2024

IITR's flagship CTF event

## Solved Challenges

| Name | Category | Points | Comment
| --- | --- | --- | --- 
| Welcome | Misc | 10 | discord lol
| [I Like McDonalds](./cry/mcd/) | Cry | 100 | hash-collision/pwntools
| [Cursed Credential](./for/cursed_credentials/) | For | 100 | firefox-login/bruteforce
| [Torrent Tempest](./for/torrent/) | For | ??? | pyshark/deepsound

## Comments/Learning

**Forensics**: 

Most of the forensics challenges had to be bruteforced in some manner and were more
steganography heavy than is expected, especially a 24hr ctf. I learnt about 2 common
forensics challenges that are the firefox credential logins (`firepwd.py`) and XORing 2 images, though
the challenges here were a level above the standard. Also `binwalk` works for extracting very small files 
a `.pcap`. That's how I got the `key.txt` in torrent chal

Looking at writeups I saw something called `deepsound` exists for `.wav` steg, and `hashcat` for password cracking. 
Apparently `hashcat` uses "Rulesets" which were mentioned in the boss's boss chal.
The torrent chal apparently had a zip header that I didn't recognise, that would have helped
reconstruct the files.

\- [@Majestic9169](https://github.com/Majestic9169)

## Writeups/Resources

### Forensics

- [k.eii](https://1keii.vercel.app/posts/backdoor-ctf-2024/)
- [thmai11](https://github.com/thmai11/writeups/tree/main/backdoorctf)
- [MindCrafters](https://kerszl.github.io/hacking/walkthrough/ctf/ctf-backdoorctf-torrent/)
- [MQCyberSec](https://seall.dev/posts/backdoorctf2024)

### Crypto

- [kh4rg0sh](https://github.com/kh4rg0sh/kh4rg0sh.github.io)
- [L3G10N](https://discord.com/channels/916568950375059476/916693278701781103/1320760127741231186)

### Web 

- [MQCyberSec](https://seall.dev/posts/backdoorctf2024)
- [Dr4g0n](https://discord.com/channels/916568950375059476/916693363045072906/1320763741163229184)
  - more specifically he points to this [blog](https://blog.huli.tw/2024/09/07/en/idek-ctf-2024-iframe/)

### Pwn

- [ADA INDONESIA COY (winners)](https://hyggehalcyon.gitbook.io/page/ctfs/2024/backdoorctf)


