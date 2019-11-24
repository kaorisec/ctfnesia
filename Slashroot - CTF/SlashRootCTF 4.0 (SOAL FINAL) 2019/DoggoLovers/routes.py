from flask import render_template, redirect, url_for, flash
from main import app
from forms import InputForm
from modules.cookie import Cookie
from base64 import b64encode, b64decode
import random
from os import path
import random, string

@app.route('/', methods=['GET', 'POST'])
def index():
    cookie_secret = init_secret()
    cookie = Cookie()
    form = InputForm()
    pic = str(random.randint(1, 5)) + ".png"
    if form.validate_on_submit():
        data = form.name.data
        datas = {'name': data, 'pic': pic}
        flash('Guk guk, namaku {}!!!'.format(datas['name']))
        cookie_ = cookie.set_cookie(data, cookie_secret)
        response = redirect(url_for('index'))
        response.set_cookie('data', cookie_)
        return response
    data = cookie.get_cookie(cookie_secret)
    return render_template('index.html', form=form, pic=pic)

def init_secret():
    if not path.exists('secret'):
        with open("secret", "w") as f:
                secret = "slashrootctf_" + ''.join(random.choice(string.digits) for x in range(3))
                f.write(secret)
    with open("secret", "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port="7576")
