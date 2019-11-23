from Crypto.Cipher import AES
import sys
import binascii
import random

IV = "4n0t3rkeybr0sist"

def encrypt(msg,phrase):
    aes = AES.new(phrase, AES.MODE_CBC,IV)
    return aes.encrypt(msg)


W = 5
perm = range(W)
random.shuffle(perm)
msg = open("rawkey.txt").read().strip()
raw = open("rawkey.txt").read().strip()
while len(msg) % (2*W):
    msg += "."

for i in xrange(100):
    msg = msg[1:] + msg[:1]
    msg = msg[0::2] + msg[1::2]
    msg = msg[1:] + msg[:1]
    res = ""
    for j in xrange(0, len(msg), W):
        for k in xrange(W):
            res += msg[j:j+W][perm[k]]
    msg = res
print "I think this is safe enough: " + msg
key = raw
data = binascii.hexlify(encrypt(sys.argv[1],key))
print "secured flag: " + data
