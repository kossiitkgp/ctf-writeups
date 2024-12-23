import pwn
import codecs
import re

words = [
    "Apple", "Breeze", "Candle", "Dolphin", "Echo", "Forest", "Galaxy", 
    "Harmony", "Island", "Journey", "Kite", "Lantern", "Mountain", 
    "Nectar", "Ocean", "Puzzle", "Quasar", "Rainbow", "Sunset", 
    "Thunder", "Umbrella", "Velvet", "Whisper", "Xylophone", "Yonder", 
    "Zephyr", "Acorn", "Blossom", "Cactus", "Dream", "Ember", 
    "Feather", "Giraffe", "Horizon", "Illusion", "Jigsaw", 
    "Kaleidoscope", "Lullaby", "Meadow", "Nightingale", "Oasis", 
    "Petal", "Quicksand", "Riddle", "Starfish", "Tapestry", 
    "Universe", "Vortex", "Willow", "Xenon", "Yearn", "Zenith", 
    "Amethyst", "Change this word", "Cascade", "Dusk", "Teri maa ki", "Fable", 
    "Glimmer", "Hummingbird", "Infinity", "Jolt", "Kismet", "Luminary"
]

HOST = "34.42.147.172"
PORT = "8004"
r = pwn.remote(HOST, PORT)

for i in range(64):
    print(r.recvuntil(b'token:').decode())
    WORD = words[i]
    HEX_WORD = codecs.encode(WORD.encode(), "hex").decode()
    # print(f"{HEX_WORD=}")
    TOKEN = HEX_WORD
    OUTPUT = f"{HEX_WORD} {TOKEN}"
    print(OUTPUT)
    r.sendline(OUTPUT.encode())
    RETURN_STRING = r.recvline().decode()
    print(RETURN_STRING)
    # NEW_TOKEN = RETURN_STRING.split("Expected token: ")[1].strip()
    MATCH = re.search(r'Expected token: (\w+)', RETURN_STRING)
    if MATCH:
        NEW_TOKEN = MATCH.group(1)
        # print(NEW_TOKEN)
    else:
        NEW_TOKEN = TOKEN
    NEW_OUTPUT = f"{HEX_WORD} {NEW_TOKEN}"
    print(r.recvuntil(b'token:').decode())
    print(NEW_OUTPUT)
    r.sendline(NEW_OUTPUT.encode())
print(r.recvall().decode())
