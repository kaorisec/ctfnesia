import hmac
import hashlib

def sha256_digest(data, secret):
    h = hmac.new("slashrootctf", data+secret, hashlib.sha256).hexdigest()
    # return sha256(data + secret).hexdigest()
    return h