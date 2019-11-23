import os
import sys
import time
import random
import string

if len(sys.argv) < 2:
  print("usage: %s <file to encrypt>" %(os.path.basename(__file__)))
  sys.exit()

rr = random.randint(0,255)
st = "".join(random.choice(string.ascii_lowercase+string.digits)for _ in range(4))

ec = "|wahihi|\n"
for c in open(sys.argv[1]).read():
  ec += chr(ord(c)^rr)

ww = open(sys.argv[1]+".enc","w+")
ww.write(ec)
ww.close()

os.system('openssl aes-256-cbc -salt -a -e -pass pass:'+st[::-1]+' -in '+sys.argv[1]+'.enc -out '+sys.argv[1]+'.wahihi')
os.system('rm '+sys.argv[1]+'.enc')

print("encrypting file ...")
print("your unique ID: %s" %(st))
print("file encrypted, have a nice day:)")