from flask import Flask, request, render_template
from firebase import firebase

import sys

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://smartkeyrack.firebaseio.com/', None)

@app.route('/')
def index():
    keys = firebase.get('/keys', None)
    key1 = keys['key1']
    key2 = keys['key2']
    key3 = keys['key3']
    key4 = keys['key4']
    return render_template('index.html', key1 = key1, key2 = key2, key3 = key3, key4 = key4)
'''
@app.route('/update', methods=['GET', 'PUT'])
def update():
    if request.method == 'GET':
        print("get")
        keys = ['key1', 'key2', 'key3', 'key4']
        for k in keys:
            val = request.args.get(k)
            if val:
                firebase.patch('/keys/', {k: val})
    if request.method == 'PUT':
        print("put")
        json = request.get_json()
        keys = ['key1', 'key2', 'key3', 'key4']
        for k in keys:
            val = json.get(k, None)
            if val:
                firebase.patch('/keys/', {k: val})
    return 'lol'
'''

@app.route('/update', methods=['POST'])
def update():
    req_data = request.get_json()
    if request.method == 'POST':
        keys = ['key1', 'key2', 'key3', 'key4']
        for k in keys:
            val = req_data.get(k, None)
            if val:
                firebase.patch('/keys/', {k: val})
    return req_data

if __name__ == '__main__':
    app.run()
