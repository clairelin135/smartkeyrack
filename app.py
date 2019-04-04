from flask import Flask, request

app = Flask(__name__)

keys = ['key1', 'key2', 'key3', 'key4']
request_vals = {}
for k in keys:
    request_vals[k] = 'Not home'

@app.route('/')
def index():
    str = ""
    for k in keys:
        str += k + " " + request_vals[k]
    return '''<h1>{}</h1>'''.format(str)

@app.route('/update')
def update():
    for k in keys:
        request_vals[k] = keys[k]

if __name__ == '__main__':
    app.run()
