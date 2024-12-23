# Cursed Credential

Points: 100

> I forgot my Browser's saved password although a friend of mine tells that I can find it if I know my master key. The problem is I dont even remember that, hopefully you can rock your brain and help me out.

`Author: W01f`

---

We are given a firefox profile that contains `cert9.db`, `key4.db`, and `logins.json`

There are many tools to decrypt the stored passwords, but they all need 
your Master Password, which we don't have. 

After a long time I raised a ticket asking if we were supposed to bruteforce
the master password, which they replied with yes. Also in the description
it would normally be _"rack"_ your brain, but they wrote _"rock"_. This was a 
reference to the "RockYou" password leak. 

So I used [FireMaster](https://securityxploded.com/download-software.php?name=firemaster) (windows tool) to bruteforce the Master Password from the [RockYou passwords list](https://github.com/zacheller/rockyou) by

```sh
wine ./FireMaster/FireMaster.exe -d -f ./FireMaster/rockyou.txt ./7glfqj3r.default-release/
```

After 9 hours this gave me the Master Password `phoenixthefirebird14`

![](./image.png)

inputting this when using [firepwd](https://github.com/lclevy/firepwd/tree/master) as 
```sh
python firepwd.py -d ./7glfqj3r.default-release/ -p phoenixthefirebird14
```

gave me the flag. Here is the full output

```sh
globalSalt: b'3510a742f59b198e198922f0c9bc43cf8ab52bf3'
 SEQUENCE {
   SEQUENCE {
     OBJECTIDENTIFIER 1.2.840.113549.1.5.13 pkcs5 pbes2
     SEQUENCE {
       SEQUENCE {
         OBJECTIDENTIFIER 1.2.840.113549.1.5.12 pkcs5 PBKDF2
         SEQUENCE {
           OCTETSTRING b'dadd3df784b946b13619b7f09fdce2e7a34e3e0cd4069263a0517d683d003695'
           INTEGER b'2710'
           INTEGER b'20'
           SEQUENCE {
             OBJECTIDENTIFIER 1.2.840.113549.2.9 hmacWithSHA256
           }
         }
       }
       SEQUENCE {
         OBJECTIDENTIFIER 2.16.840.1.101.3.4.1.42 aes256-CBC
         OCTETSTRING b'6bb3481d3086ee025f5b4b5b0afb'
       }
     }
   }
   OCTETSTRING b'9c55609a7548c032b1bee0a1d948cec5'
 }
clearText b'70617373776f72642d636865636b0202'
password check? True
 SEQUENCE {
   SEQUENCE {
     OBJECTIDENTIFIER 1.2.840.113549.1.5.13 pkcs5 pbes2
     SEQUENCE {
       SEQUENCE {
         OBJECTIDENTIFIER 1.2.840.113549.1.5.12 pkcs5 PBKDF2
         SEQUENCE {
           OCTETSTRING b'206809d983c25581358938922066ac024e4c0647dc40a0a6a359b953912391d6'
           INTEGER b'2710'
           INTEGER b'20'
           SEQUENCE {
             OBJECTIDENTIFIER 1.2.840.113549.2.9 hmacWithSHA256
           }
         }
       }
       SEQUENCE {
         OBJECTIDENTIFIER 2.16.840.1.101.3.4.1.42 aes256-CBC
         OCTETSTRING b'7e15be87cb1d151cf4010a722b08'
       }
     }
   }
   OCTETSTRING b'03dbf91b20365af4f4fc7b27187b2e8e8c466e1de66c30e78496299db4827b68'
 }
clearText b'6d100851c72a9226fb8057011ffd23bae5f42f54b33746160808080808080808'
decrypting login/password pairs
https://play.picoctf.org:b'4n0nym0u5',b'flag{n0_p@ssw0rd_15_s3cur3??}'
```

```
flag{n0_p@ssw0rd_15_s3cur3??}
```
