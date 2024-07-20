#!/usr/bin/env python

from Crypto.Cipher import AES
import hashlib

enc_string = b'\x16\x97,\xa7\xfb_\xf3\x15.\x87jKRaF&"\xb6\xc4x\xf4.K\xd77j\xe5MLI_y\xd96\xf1$\xc5\xa3\x03\x990Q^\xc0\x17M2\x18'

FLAG_HASH = "6a96111d69e015a07e96dcd141d31e7fc81c4420dbbef75aef5201809093210e"

print(f'FLAG_HASH = {FLAG_HASH}')

for i in range(128):
    key = b'the_enc_key_is_'
    key += i.to_bytes(1, 'big')
    for j in range(128):
        iv = b'my_great_iv_is_'
        iv += j.to_bytes(1, 'big')
        decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = decrypt_cipher.decrypt(enc_string)
        flag_hash = hashlib.sha256(plaintext[:32]).hexdigest()
        if flag_hash == FLAG_HASH:
            print(f'flag_hash = {flag_hash}')
            print(f'dec is {plaintext[:32]}')
