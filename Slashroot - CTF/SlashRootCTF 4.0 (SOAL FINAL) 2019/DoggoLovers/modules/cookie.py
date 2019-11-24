from flask import redirect, url_for, request, flash
from base64 import b64encode, b64decode
from modules.sha256_digest import sha256_digest
import pickle


class Cookie:
    def set_cookie(self, data, secret):
        data = b64encode(pickle.dumps(data))
        cookie =  str(sha256_digest(data, secret)) + ":" + data
        return cookie

    def get_cookie(self, secret):
        cookie = request.cookies.get('data')
        if not cookie:
            return ''
        cookie = cookie.split(":")
        hash_digest = cookie[0]
        data = cookie[1]
        if not sha256_digest(data, secret) == hash_digest:
            flash('Maaf cookie anda tidak valid!')
            return False
        return pickle.loads(b64decode(data))
