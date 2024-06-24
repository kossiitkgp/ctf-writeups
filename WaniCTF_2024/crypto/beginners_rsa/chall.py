from Crypto.Util.number import *
import binascii

p = getPrime(64)
q = getPrime(64)
r = getPrime(64)
s = getPrime(64)
a = getPrime(64)
n = p*q*r*s*a
w = (p-1)*(q-1)*(r-1)*(a-1)*(s-1)  # added by me
e = 0x10001

FLAG = b'FLAG{This_is_a_fake_flag}'
m = bytes_to_long(FLAG)
enc = pow(m, e, n)
d = inverse(e, w)  # added by me
dec = pow(enc, d, n)  # added by me
print(f'n = {n}')
print(f'e = {e}')
print(f'enc = {enc}')

# everything after this was added by me in my descent to madness

print(f'dec = {pow(enc, d, n)}')
print(f'm = {m}')
print(binascii.unhexlify(str(hex(dec)[2:])))

r1 = p  # 9482511096791297231
r2 = q  # 9968364261574843559
r3 = r  # 10439133972833708741
r4 = s  # 15347332940292778669
r5 = a  # 18132295091947302697

ri = [r1, r2, r3, r4, r5]

n = r1*r2*r3*r4*r5

enc = 520429879581651146398839876539275386478124453765795617322423469101666595210652435006889762667

k = len(ri)

di = []
for i in ri:
    di.append(inverse(e, i - 1))


m = ri[0]
ti = [0]

for i in range(1, k, 1):
    ti.append(inverse(m, ri[i]))
    m = m*ri[i]

xi = []

for i in range(k):
    xi.append(pow(enc % ri[i], di[i], ri[i]))

x = xi[0]
m = ri[0]

for i in range(1, 3):
    if x < m and pow(x, e, m) == enc:
        break
    else:
        x = x + m*(((xi[i] - (x % ri[i]))*ti[i]) % ri[i])
        m = m*ri[i]
        print(f'x = {x}')


for i in range(k):
    print(str(ri[i]) + ' = r' + str(i+1))
    print(str(di[i]) + ' = d' + str(i+1))
    print(str(ti[i]) + ' = t' + str(i+1))
    print(str(xi[i]) + ' = x' + str(i+1))

print(binascii.unhexlify(str(hex(x)[2:])))
