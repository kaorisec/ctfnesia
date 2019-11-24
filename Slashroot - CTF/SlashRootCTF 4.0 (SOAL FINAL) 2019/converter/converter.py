#!/usr/bin/env python
from re import findall
from base64 import b64decode, b64encode
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

def tydac_ada_sistem_yang_aman():
        tIdaK_aDa_sIstEm_yAng_aMan = ['open',
        'file',
        'execfile',
        'compile',
        'reload',
        '__import__',
        'input',
        ]
        for sistem_yang_aman in tIdaK_aDa_sIstEm_yAng_aMan:
            del __builtins__.__dict__[sistem_yang_aman]

def welcome():
    return """ ___ _                   ____  ____
|_ _| |    _____   _____/ ___||  _ \
 | || |   / _ \ \ / / _ \___ \| |_) |
 | || |__| (_) \ V /  __/___) |  _ <
|___|_____\___/ \_/ \___|____/|_| \_\\
"""

def main():
    while True:
        print """
1. Hex2Dec
2. Dec2Hex
3. B64Encode
4. B64Decode
        """
        inp = raw_input("Choice: ")
        if inp == '1':
            try:
                jangan = 'GHIJKLMNOPQRSTUVWYZgijklmnopqstuvwyz_~`!@#$%^&*-={[:"\'\\]}'
                hexa = raw_input("Input hex, starts with '0x'\n")
                for i in hexa:
                    if i in jangan:
                        print "NgEHeK kOk pAkE tErmOS"
                        exit()
                exec "print " + str(eval(hexa))
            except Exception, error:
                print "Exception: ", error
        elif inp == '2':
            try:
                dec = int(raw_input("Input a decimal number\n"))
                print hex(dec)
            except ValueError:
                print "Please input a decimal number"
        elif inp == '3':
            try:
                string = str(raw_input("Input some shit to encode\n"))
                print b64encode(string)
            except Exception:
                print Exception
        elif inp == '4':
            try:
                encoded = str(raw_input("Input some base64 encoded shit to decode\n"))
                print b64decode(encoded)
            except Exception:
                print Exception

if __name__ == "__main__":
    sys.stdout = Unbuffered(sys.stdout)
    tydac_ada_sistem_yang_aman()
    print welcome()
    main()
