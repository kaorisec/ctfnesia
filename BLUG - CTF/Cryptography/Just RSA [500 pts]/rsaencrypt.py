from Crypto.Util.number import *

e1 = 9
e2 = 123
 
def generet_prima():
    while True:
        p = getPrime(1024)
        q = getPrime(1024)
        n = p*q
        phi_n = (p-1)*(q-1)
        if GCD(e1, phi_n) == 1 and GCD(e2, phi_n) == 1:
            return (p, q, n)
p, q, n = generet_prima()
 
print "p: ", p
print "q: ", q
print "n: ", n
 
bendera = bytes_to_long(open("flag.txt").read().strip())
assert bendera < n  
assert bendera**9 > n
 
c1 = pow(bendera, e1, n)
c2 = pow(bendera, e2, n)
 
print "c1: ", c1
print "c2: ", c2