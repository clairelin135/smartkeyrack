from flask import Flask, request, render_template
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
    return render_template('index.html', key1 = key1, key2 = key2, key3 = key3, key4 = key4)

@app.route('/update')
def update():
    keys = ['key1', 'key2', 'key3', 'key4']
    for k in keys:
        val = request.args.get(k)
        if val:
            #firebase.put('/keys/' + k, val, {'print': 'silent'})
            #firebase.put('/keys/' + k, val, {'print': 'silent'})
            firebase.patch('/keys/', {k: val})
    return 'lol'

if __name__ == '__main__':
    app.run()
