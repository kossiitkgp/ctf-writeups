# niteCTF 2024

CryptoNite MIT's flagship CTF

## Challenges

| Name | Category | Points | Comments
| --- | --- | --- | ---
| Warmup | Misc | 10 | lol
| [Mumbo Dumbo](./ai/mumbo-dumbo/) | AI | 50 | llm
| Cybernotes | Web | 50 | jwt tampering
| [BackTrack](./osint/backtrack/) | Misc | 50 | osint
| [La Casa de Papel](./cry/la_casa_de_papel/) | Cry | 50 | hash length extension apparently
| [RSAabc](./cry/rsabc/) | Cry | 50 | rsa (obv)
| [Tet-reffic](./for/tet_reffic/) | For | 231 | just missed it (USB pcap)

## Comments/Learnings

Mine the Cap was a very interesting challenge to me and emphasised the importance of
python scripting. The intended solve was to examine the protocol and manually create a packet
parser that would give us block data. Something like this is kind of rare in forensics chals.
Buckspeak looked cool too, I wanted to do something more about the bucking cipher.

Other than that nothing super interesting comes to mind really, I learnt that proof of work (pow) is a thing
in mumbo dumbo ig. If I had to say something then the hash length thingy in la casa 
looked interesting, but the challenge didn't require any of that so I'm not really interested rn ig

\- [Majestic9169](https://github.com/Majestic9169)

## Writeups/Resources Dump

```
pwn/rev ish
https://qiita.com/schectman-hell/items/23ba2c244ad466fe1a90
for
https://yun.ng/c/ctf/2024-nitectf/
osint?
https://github.com/devarjya27/CTF_writeups/tree/main/niteCTF%202024
for
https://kerszl.github.io/hacking/walkthrough/ctf/ctf-nitectf-BuckSpeak/
hardware
https://abuctf.github.io/posts/NiteCTF2024/
web
https://sibivasan.gitbook.io/sibivasan/writeups/2024/nitectf-2024
hardware
https://github.com/Trixai/niteCTF2024-Writeups/blob/main/Seek_Quence.md
ai
https://github.com/IssaBoudin/CTF_WriteUps/blob/main/Mumbo_Dumbo_README.md
pwn/rev?
https://4n0nym4u5.tech/blog/nite_ctf_2024/
official
https://github.com/Cryptonite-MIT/niteCTF-2024/
```
