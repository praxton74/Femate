from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getdata():
    name = request.form['name']
    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
    s = name
    payload = {
        "enable_google_results": False,
        "enable_memory": False,
        "input_text": s
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": "2703d90c-bcdc-4d20-9eb2-d429138d850b"
    }

    response = requests.post(url, json=payload, headers=headers)

    str = response.text
    res = str.partition(",")[0]
    print(str)
    return render_template('index.html', value=str[11:])


if __name__ == '__main__':
    app.run(debug=True, port=7000)
