from Crypto.Cipher import ARC4
from SlashRootCTF import FLAG, KEY, I
from art import *
from base64 import b64encode as b64e, b64decode as b64d
from hashlib import sha1 as checksum
from numpy.random import choice, seed as seat
from string import letters
from time import time as now
import sys


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)


class RC4:
    def __init__(self, key):
        self.salt = choice(list(letters), [4, 4]).tostring()
        self.key = key

    def rc(self):
        key = self.salt + self.key
        return ARC4.new(key[:40])

    def encrypt(self, plaintext):
        return b64e(self.salt + self.rc().encrypt(code(plaintext)))

    def decrypt(self, ciphertext):
        try:
            salt = self.salt
            data = ["invalid"]
            dec = b64d(ciphertext)
            self.salt = dec[:len(self.salt)]
            enc = xor(self.rc().decrypt(dec[len(self.salt):]))
            data += enc.split("|")
            if len(data) > 4:
                data.remove("invalid")
        finally:
            if "invalid" in data:
                self.salt = salt
            return data


def code(data):
    return xor("|".join(data))


def xor(text):
    return "".join(chr(ord(char) ^ I) for char in text)


def validate(data):
    sh = data.pop()
    if checksum(str(data)).hexdigest() == sh:
        return True
    else:
        return False
try:
    scheduled = int(now())
    seat(scheduled)
    rc = RC4(KEY)
    ticket = rc.decrypt(raw_input(welcome(scheduled)))
    if "invalid" in ticket:
        free = raw_input(" Wanna Free Ticket? [y/N] ")
        if free.lower() == "y":
            data = ["free", "guest"]
            data.append(str(scheduled + 60))
        else:
            data = ["book"]
            data.append(raw_input(" Booking NOW!!!\n Name: "))
            data.append(str(scheduled + 60**2*4*4))
        data.append(checksum(str(data)).hexdigest())
        print " Your Ticket:", rc.encrypt(data),
    else:
        if ticket[0] == "flag":
            flag = FLAG
        elif ticket[0] == "book":
            if validate(ticket) and "flag" in ticket:
                if int(now()) > int(ticket[2]):
                    flag = FLAG
                else:
                    flag = "ToO SoOn"
            else:
                flag = ticket[1]
        else:
            flag = ""
        congrat(flag)
        if flag == FLAG:
            getKey()
except Exception:
    glhf()
finally:
    goodbye()

