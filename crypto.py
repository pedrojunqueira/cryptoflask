from flask import Flask, render_template, url_for, redirect, request
import requests

url = f'https://apiv2.bitcoinaverage.com/indices/global/ticker/'

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def receive():
    #form = ConvertForm()
    if request.method == 'POST':
        crypto = request.form.get("crypto")
        fiat = request.form.get("fiat")
        r = requests.get(url+crypto+fiat)
        price = r.json()['last']
        return render_template('result.html', price=price, crypto=crypto, fiat=fiat)
    return render_template('receive.html')

@app.route("/result", methods=['GET', 'POST'])
def result():

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
