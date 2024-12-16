# BackTrack

Points: 50

__OSINT__

> Kenji is a nice guy who lives in Tokyo. He is in a dilemma. In 2017, he was late to an important meeting and is now facing repercussions. To defend himself, he needs to prove that it was not his fault...

Author: kua_23

---

First thing I searched for, was about the stations Omotesando and Suitengumae. This led me to conclude that these were connected by Tokyo Metro.<br/>

To lookup for the schedules of metro, I visited the [Tokyo Metro Website](https://www.tokyometro.jp/lang_en/index.html) which had many lines. I searched for the stations Omotesando and Suitengumae on Google and found that Hanzomon line connects them both. Now, I needed to look at some past delay records.<br/>

I found a section called [Delay Certificates](https://www.tokyometro.jp/lang_en/delay/history/hanzomon.html) on the metro website and it was the treasure! I needed 2017 data, so I looked up on Internet Archive for Delay Certificates (for Hanzomon line). Starting from January 2017, I went upto March and found the **61 minute** delay record on February 2017 [here](https://web.archive.org/web/20170326043929/https://www.tokyometro.jp/lang_en/delay/history/hanzomon.html)<br/>

```
flag: nite{17:00_20February}
```