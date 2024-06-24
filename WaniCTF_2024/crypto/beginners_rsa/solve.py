from Crypto.Util.number import *
import binascii

p = 9953162929836910171
q = 11771834931016130837
r = 12109985960354612149
s = 13079524394617385153
a = 17129880600534041513

n = p*q*r*s*a

w = (p-1)*(q-1)*(r-1)*(s-1)*(a-1)

e = 0x10001

enc = 127075137729897107295787718796341877071536678034322988535029776806418266591167534816788125330265

d = inverse(e, w)

dec = pow(enc, d, n)

print(binascii.unhexlify(str(hex(dec)[2:])))
