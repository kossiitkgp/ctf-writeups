# Too Hidden

Points: 150

> I just found some suspicious traffic in my system. Hmmmmmmmmmmm I hope that it is harmless…

`Author: Odin`

---

There were some `ARP` packets (address resolution protocol) and a lot of `ICMP` packets

quick searches for "ICMP ctf" gave a lot of possible vulnerabilities with ICMP, like ICMP tunnelling etc. [More](https://www.packetsafari.com/blog/2023/01/13/ctf-pcap-challenges/)

they basically contain very little data and only in the last byte somewhere

if you went through the packets you could see the were changing very little, and the data
was only taking 3-4 different values

we can extract the values with tshark

```sh
tshark -Y "icmp.ident == 0 && icmp.type == 8" -T fields -e data.data -r chall.pcapng | awk '{printf "%s", $1}' | xxd -r -p | xxd -r -p
```

this one liner was from an article, sadly i can't find it right now. Anyway all it is doing is 
taking those data bytes from the packets and converting them to ascii

anyway that gives us `FEE2FEE2FFEF22FFFF2EEE2FEFF2EFEE2FFEEFE2FFF2FFFF2F2F2F2F2E2FFEEFE2EFEE2EEE2FFE2FFEEFE2EFEF2FE2EF2FFEEFE2FFEF2FF2EF2EFF2FFEEFE2EE2F2FFEEFE2FFEEFF2FFEEFF2FFEEFF2FFEEFF2FFEEFF2FFEEFF2FFEEFF2FFEEFF2FFEEFF2FFEEFF2`

Now the challenge name was 'Too Hidden', the "Too" and the "2" clicked something and made
me think of morse with 2 as the word delimiter. also to confirm, `FEE` would be `W`

converting to morse gives 
`.-- .-- ..-.  .... --- .-.. -.-- ..--.- ... .... . . . . - ..--.- -.-- --- ..- ..--.- -.-. .- -. ..--.- ..-. .. -. -.. ..--.- -- . ..--.- ..--.. ..--.. ..--.. ..--.. ..--.. ..--.. ..--.. ..--.. ..--.. ..--.. `

which decodes to `WWF{HOLY_SHEEEET_YOU_CAN_FIND_ME_??????????}`

---

```sh
wwf{HOLY_SHEEEET_YOU_CAN_FIND_ME_??????????}
```
