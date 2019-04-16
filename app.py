from flask import Flask, request, render_template, redirect, url_for
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://smartkeyrack.firebaseio.com/', None)

@app.route('/')
def index():
    keys = firebase.get('/keys', None)
    key1 = keys['key1']
    key2 = keys['key2']
    key3 = keys['key3']
    key4 = keys['key4']
    return render_template('index.html', key1=key1, key2=key2, key3=key3, key4=key4)

@app.route('/edit')
def edit():
    keys = firebase.get('/keys', None)
    key1 = keys['key1']
    key2 = keys['key2']
    key3 = keys['key3']
    key4 = keys['key4']
    return render_template('edit.html', key1=key1, key2=key2, key3=key3, key4=key4)

@app.route('/submit', methods=['POST'])
def submit():
    keys = firebase.get('/keys', None)
    key_statuses = {
        'key1': keys['key1'],
        'key2': keys['key2'],
        'key3': keys['key3'],
        'key4': keys['key4']
    }
    if request.method == 'POST':
        keys = ['key1', 'key2', 'key3', 'key4']
        for k in keys:
            newname = request.form[k]
            if newname:
                payload = {
                    'name': newname,
                    'status': key_statuses[k]['status']
                }
                firebase.patch('/keys/' + k + '/', payload)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    keys = firebase.get('/keys', None)
    key_statuses = {
        'key1': keys['key1'],
        'key2': keys['key2'],
        'key3': keys['key3'],
        'key4': keys['key4']
    }
    req_data = request.json
    if request.method == 'POST':
        keys = ['key1', 'key2', 'key3', 'key4']
        for k in keys:
            val = req_data.get(k, None)
            if val:
                payload = {
                    'name': key_statuses[k]['name'],
                    'status': val
                }
                firebase.patch('/keys/', {k: payload})
    return req_data or "None"

if __name__ == '__main__':
    app.run()
