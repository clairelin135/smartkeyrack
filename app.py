from flask import Flask, request, render_template

app = Flask(__name__)

keys = ['key1', 'key2', 'key3', 'key4']
request_vals = {}
for k in keys:
    request_vals[k] = 'Not home'

@app.route('/')
def index():
    return render_template('index.html', key1 = request_vals[keys[0]], key2 = request_vals[keys[1]], key3 = request_vals[keys[2]], key4 = request_vals[keys[3]])

@app.route('/update')
def update():
    for k in keys:
        if request.args.get(k):
            request_vals[k] = request.args.get(k)

if __name__ == '__main__':
    app.run()
