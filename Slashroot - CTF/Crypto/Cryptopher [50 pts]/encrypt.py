import base64

def encrypt(plaintext):
    flag = ""
    for i, j in enumerate(plaintext):
           flag += chr(((ord(j) ^ i) + 1) % 127)
    
    return base64.b64encode(flag)



flag = "- R E D A C T E D -"

print encrypt(enc)