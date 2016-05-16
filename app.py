# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request, url_for

from encryption import encode, decode

#Create app
app = Flask(__name__)
app.secret_key = 'w3ioreadfkl;"JPO#L:RWEK"afo2q243awije"LMK?FSA":K@#"%:RQEFASKF{OEWJT@$ntlwefadczx,mdvklsf}'

#Define variables for templates
website_name = 'Flask App'

#Index/Home/Land

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt')
def encrypt():
    return render_template('encrypt.html')

@app.route('/decrypt')
def decrypt():
    return render_template('decrypt.html')

@app.route('/encrypt_result', methods=['POST'])
def encrypt_result():
    data = dict(request.form.items())
    
    message = encode(data['message'], data['password'])
    
    return render_template('result.html', message=message)

@app.route('/decrypt_result', methods=['POST'])
def decrypt_result():
    data = dict(request.form.items())
    
    message = decode(data['message'], data['password'])
    
    return render_template('result.html', message=message)

if __name__ == "__main__":
    import os
    app.run(port=os.environ['PORT'], host=os.environ['IP'])