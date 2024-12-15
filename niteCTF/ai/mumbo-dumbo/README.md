
# Mumbo Dumbo

Points: 50

__ai__

> Deep within the void lies the Key, shrouded in secrecy and guarded by the enigmatic Keeper. Created for a single purpose, the Keeper has vowed to protect the Key, its defenses said to be unbreakable.
> But whispers tell of a flaw-a hidden crack in its impenetrable armor. Those who dare to seek the Key must tread lightly, for the Keeper is cunning and relentless, answering only to the most devious of minds.
> Will you uncover the Keeper's secret, or be lost in the void forever?

Author : evelynhvgo

```sh
ncat --ssl mumbo-dumbo.chals.nitectf2024.live 1337
```

---

We are given `pow.py` which is a proof-of-work function being used to enter the challenge instance ig. Not entirely sure what the purpose is.

We are dropped into a covnersation with an extremely medieval and annoying LLM that on probing a little reveals that it was commanded to not answer anything unless the phrase

"elephant in the room"

is uttered 

```
flag: nite{C@TCHME!FY0UCAN}
```
